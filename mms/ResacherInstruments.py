# -*- coding: cp1251 -*-

# ------- measurement and data processing --------------------
import math
#import matplotlib.pyplot as plt
#import matplotlib.ticker
#import pylab

class Table:
    obtG = []   # model tackt
    obt = []    # time in the rest system
    obx = []    # particle coordinate 
    localT = []  # local time of cell
    particleT = [] # particle time
    pulse = 0
    pulseT = []   # interection acts 
    
    def __init__(self):
        pass

    # x,t - coordinate fixed
    def fixIt(self,tG, tt, xx, locT, prtT):
        self.obtG.append(tG)
        self.obt.append(tt)
        self.obx.append(xx)
        self.localT.append(locT)
        self.particleT.append(prtT)

    # force detect
    def detect(self, tG, c):
        if not (c is None): 
            pulse = 1   # force - we use 1 force
        else:
            pulse = 0
        self.pulseT.append(pulse)

    def rewriteIt(self,tG, tt, xx, locT, prtT):
        #pop(i) удаляет элемент с индексом i и возвращает его.
        #Если вызвать pop() без параметров, то будет возвращён
        #и удалён последний элемент списка
        self.obtG.pop()
        self.obtG.append(tG)
        self.obt.pop()
        self.obt.append(tt)
        self.obx.pop()
        self.obx.append(xx)
        self.localT.pop()
        self.localT.append(locT)
        self.particleT.pop()
        self.particleT.append(prtT)

    def dataControl(self):
        for i in range(0,self.countTick):
            if self.obtG[i] <> self.localT[i]:
                print "No sync:obtG[i] <> localT[i]: ",i, self. obtG[i], self.localT[i]
            if self.obtG[i] <> self.localT[i]:
                print "No sync:obtG[i] <> particleT[i]: ",i, self. obtG[i], self.particleT[i] 
        

class DataProcessing:
    obs = None
    particle_velosety = None
    sizeTick = None
    countTick = None
    mass = 1 # mass of particle (natural)
    lightVel = 1.0 # light velocity
    nu_t = 0.0  # time coefficient of conversion
    nu_x = 0.0  # length coefficient of conversion
    nu_m = 0.0  # mass coefficient of conversion 

    x = []
    t = []
    t_err = []
    t_acc = []
    t_local_err = []

    
    vel_t = []      # experimental value of velocity
    vel_t_err = []  # experimental error measurement
    velAnl = []     # analytical velocity as function from momentum

    momentum_t = []
    eng_t_acc = []
    eng_t = []
    eng_t_err = []
    
    def __init__(self, ob, v, st, ct):
        self.obs = ob
        self.particle_velosety = v
        self.sizeTick = st
        self.countTick = ct
        # it is define of coefficient of conversion
        self.nu_m = 1.0       # mass coefficient of conversion     
        self.nu_t = float(st)  # time coefficient of conversion, 2
        self.nu_x = self.lightVel*self.nu_t  # length coefficient of conversion (then v/c)
        #self.nu_x = 10.0  # length coefficient of conversion 
        # самое достоверное 2.0*float(st) и 10
        
        #print "Resalution of model:"
        print "nu_t =", self.nu_t, ", nu_x =", self.nu_x, ", nu_m =", self.nu_m
        print "mass =", self.mass, ", lightVel =", self.lightVel
        print " "
        
        
        
    # base processing
    # t and x
    def xtCalculate(self):
        for i in range(0,len(self.obs.obtG)):
            t = float(self.obs.obt[i])/self.nu_t
            self.t.append(t)
            self.t_err.append(0.5*(1.0/2.0)/self.nu_t) # 0.5 bar
            x = float(self.obs.obx[i])/self.nu_x
            self.x.append(x)
        print "coordinate calculated"
            
    # accurate t (analytical formula)
    def xtAccurate(self):
        self.t_acc.append(0.0)
        err=0.0
        self.t_local_err.append(err)
        for i in range(1,len(self.obs.obtG)):
            an = math.sqrt(float(self.obs.obtG[i])**2+self.x[i]**2)
            self.t_acc.append(an)
            err = math.fabs(100.0*(an - self.t[i])/an)
            self.t_local_err.append(err)
        print "accurate coordinate calculated"

    # experimental value of velocity
    def velocityCalculate(self):
        self.vel_t.append(0.0)
        self.vel_t_err.append(0.0)
        for i in range(1,len(self.obs.obtG)):
            dt = float(self.obs.obt[i]-self.obs.obt[i-1])/self.nu_x
            dx = float(self.obs.obx[i]-self.obs.obx[i-1])/self.nu_x
            vv = dx/dt
            self.vel_t.append(vv)
            vve = self.velErrorCalculate(dt,dx)
            self.vel_t_err.append(vve)
        print "velocity calculated"
    # experimental error measurement of velocity
    def velErrorCalculate(self, dt, dx):
        vv=dx/dt
        del_t = (1.0/2.0)/self.nu_t
        del_x = (1.0/2.0)/self.nu_x
        varx = 1.0/dt
        vart = math.fabs(vv)/dt
        # 0.5 to errbar
        vve = 0.5*math.sqrt(2)*math.sqrt((varx*del_x)**2 + (vart*del_t)**2)
        return vve
    
        #qE = (1/self.nu_m)*(self.nu_t*self.nu_t/self.nu_x) * 1.0

    def momentumCalculate(self):
        p = 0.0
        self.momentum_t.append(p)
        self.velAnl.append(self.velAnalytical(p))
        for i in range(1,len(self.obs.obtG)):
            ddt = float(self.obs.obt[i]-self.obs.obt[i-1])
            dt = self.t[i]-self.t[i-1]
            # f = (1.0/self.nu_m)*(self.nu_t*self.nu_t/self.nu_x)*(float(self.obs.pulseT[i])/(ddt*ddt))
            # f = (1.0/self.nu_m)*(float(self.obs.pulseT[i])/(dt*self.nu_t))
            f = (1.0/self.nu_m)*(self.nu_t/float(self.sizeTick))*(float(self.obs.pulseT[i])/(float(self.sizeTick)))
            dp = f*dt
            #print self.obs.pulseT[i],f, dp
            p = p + dp
            self.momentum_t.append(p)
            self.velAnl.append(self.velAnalytical(p))
        print "momentum calculated"
    # analytical velocity as function from momentum 
    def velAnalytical(self, p):
        pp=p
        vAnl = pp/math.sqrt(self.mass**2 + (pp/self.lightVel)**2)
        # true!:
        #vAnl = p/math.sqrt(self.mass**2 + (p/1.0)**2)
        return vAnl
    # momentum
        
    def energeAccurate(self):
        m = float(self.mass)/self.nu_m  # mass
        c = self.lightVel  # light velocity
        c = 1.0 # true!
        for i in range(0,len(self.obs.obtG)):
            p = self.momentum_t[i]
            energy = math.sqrt((m**2)*(c**4) + (p*c)**2)
            self.eng_t_acc.append(energy)
        print "accurate energy calculated"
        

    def energeCalculate(self):
        m = float(self.mass)/self.nu_m  # mass
        c = self.lightVel  # light velocity
        c =1.0 # true!
        err_x = (1.0/2.0)/self.nu_x # absolute error of measurement x
        err = 0.0
        self.eng_t_err.append(err)
        energy = m*c**2  
        self.eng_t.append(energy)
        for i in range(1,len(self.obs.obtG)):
            ddt = float(self.obs.obt[i]-self.obs.obt[i-1])
            dt = self.t[i]-self.t[i-1]
            # f = (1.0/self.nu_m)*(self.nu_t*self.nu_t/(1.0*self.nu_x))* (float(self.obs.pulseT[i])/(ddt*ddt))  # force; pulseT is dp and f =dp/dt
            # f = (1.0/self.nu_m)*(float(self.obs.pulseT[i])/(dt*self.nu_t))
            f = (1.0/self.nu_m)*(self.nu_t/float(self.sizeTick))*(float(self.obs.pulseT[i])/(float(self.sizeTick)))
            dx = self.x[i] - self.x[i-1]
            dA = f*dx  # i.e. force multiple by displacement
            energy = energy + dA
            self.eng_t.append(energy)
            err = err+(0.5)*err_x*math.sqrt(2.0*f) # , where 0.5 to errbar
            self.eng_t_err.append(err)
        print "energy calculated"

    # obligatory caculation --------------------------------------------
    def baseCalculate(self):
        self.xtCalculate() #coordinates
        self.xtAccurate()
        self.velocityCalculate()
        self.momentumCalculate()
        self.energeCalculate()
        self.energeAccurate()


