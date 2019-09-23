# -*- coding: cp1251 -*-
# energy and momentum

import math

import mms
import ResacherInstruments as ri
import printResult
import graths


class originalToolkit(ri.DataProcessing):
    xAtrack = []     # track, analitical solution
    xNtrack = []     # track, numerical solution
    pA = []
    vA = []
    vN = []
    eN = []
    
    def __init__(self, observer,particle_velosety, sizeTick, countTick):
        #super.__init__(sizeTick, countTick, observer)
        ri.DataProcessing.__init__(self, observer, particle_velosety, sizeTick, countTick)

    # analytical solution of motion differential equation
    def anlSolution(self):
        m = float(self.mass)/self.nu_m
        qE = (1/self.nu_m)*(self.nu_t*self.nu_t/self.nu_x) * 1.0/float(self.sizeTick*self.sizeTick)
        print "qE=", qE
        c = self.lightVel
        for i in range(0,len(self.obs.obtG)):
            ddt = float(self.obs.obt[i]-self.obs.obt[i-1])
            x = (m*c**2/qE)*(math.sqrt(1.0+(qE*self.t[i]/(m*c))**2)-1.0)       
            self.xAtrack.append(x)
            p = qE*self.t[i]
            self.pA.append(p)
            v = p/math.sqrt(m**2 + (p/c)**2)
            jv = self.t[i]*qE/(m*c)
            v = math.sqrt(jv*jv/(1+jv*jv))*c
            self.vA.append(v)
        print "Analytical solution of the differential equation of motion"

    # Numerical solution of motion differential equation
    # Euler method 
    def numSolution(self):
        m = float(self.mass)/self.nu_m
        c = self.lightVel
        p1 = 0.0
        x1 = 0.0
        self.xNtrack.append(x1)
        self.vN.append(0.0)
        e = m*c*c
        self.eN.append(e)
        for i in range(1,len(self.obs.obtG)):
            dt = self.t[i]-self.t[i-1]
            ddt = float(self.obs.obt[i]-self.obs.obt[i-1])
            #ddt = float(self.sizeTick)
            qE = (1/self.nu_m)*(self.nu_t*self.nu_t/self.nu_x) * 1.0/float(self.sizeTick*self.sizeTick)
            #print "qE=", qE
            p2 = p1 + qE*dt
            self.vN.append(p2/math.sqrt(m**2 + (p2/c)**2))
            e = e + qE*(self.x[i]-self.x[i-1])
            self.eN.append(e)            
            v = p1/math.sqrt(m**2 + (p1/c)**2)
            x2 = x1 + v*dt        
            self.xNtrack.append(x2)
            p1 = p2
            x1 = x2
        print "Numerical solution of the differential equation of motion"

# analytical solution print
class originalPrint(printResult.TablePrint):
    def __init__(self, dp):
        #super.__init__(sizeTick, countTick, observer)
        printResult.TablePrint.__init__(self, dp)
    
    def solPrintSimple(self):
        print
        print "Analytical solution"
        for i in self.dt.obs.obtG:
            print "Tw=",i,"t =",self.dt.t[i], "x =",round(self.dt.x[i],2), "xa =",round(self.dt.xAtrack[i],2), "xe =",round(self.dt.xNtrack[i],2), "p =",self.dt.momentum_t[i], "pa=",round(self.dt.pA[i],2), "v=",round(self.dt.vel_t[i],2), "va=",round(self.dt.vA[i],2)

    def solPrintPrettyTable(self):
        print
        print "Analytical (xa, pa, va) and numerical (xe) solution"
        pt = printResult.PrettyTable(["Tw","t", "x", "xa", "xe", "p", "pa", "v", "va"])
        for i in self.dt.obs.obtG:
            pt.add_row([i, self.dt.t[i], round(self.dt.x[i],2), round(self.dt.xAtrack[i],2),round(self.dt.xNtrack[i],2),round(self.dt.momentum_t[i],2),round(self.dt.pA[i],2),round(self.dt.vel_t[i]), round(self.dt.vA[i],2) ])
        print pt

class simpleIteraction(mms.Composite):

    def __init__(self, sizeTick, countTick, particle_velosety, observer):
        #super.__init__(sizeTick, countTick, observer)
        mms.Composite.__init__(self, sizeTick, countTick, observer)
        self.__foo = None
        # particle, initial condition
        self.lst.contents = mms.Leaf(particle_velosety)
        print "Particle velosety =", particle_velosety 
        self.carr = mms.Carrier()
        self.carr.direction = 1

    # polymorthism
    def interaction(self, car):
        if not (car is None):
            if car.direction == 0:
                car.direction = 1
            else:
                car.direction = 0
        return car


# Execute -------------------
# Estimated calculation
c = 2.997925e8 # m/s
lm = 1.0/c
print "Estimated calculation for electron:"
m = 9.1e-31  # mass of electron, kg
e = 1.602e-19 #C - Coulomb, e electric charge of electron
nu_m = 1.0/m
nu_t = 10*c
f = (1.0/nu_m)*(nu_t/10.0)*(1.0/10.0)
E = f/e
print "m= ", m, " kg, e= ", e, "C"
print "nu_m = ", nu_m, "nu_t = ", nu_t
tk = m*c/f
print "f=", f, " N, E=", E, " V/m, z = ", tk,  "s "
d = (m*c/f)*(math.sqrt(1.0+(f*tk/(m*c))*(f*tk/(m*c))) - 1.0)
print "d = ", d, " m"
print " must grid ", tk, "x", d, " s x m"
print
print "In c = 1, m =1 system, f =", f/(c*m)
print

# Init parametrs section
particle_velosety = 0 # particle_velosety < sizeTick
sizeTick = 10 # size of tact (1 tick)
countTick = 9 # count of ticks
print "Parameters:"
print "countTick=",countTick, "sizeTick=", sizeTick

# Run section
observer = ri.Table()
xt= simpleIteraction(sizeTick, countTick, particle_velosety, observer)
print
print "Simulation of particle motion:"
xt.run()
print

# Data processing
print "Data processing:"
dp = originalToolkit(observer, particle_velosety, sizeTick, countTick)
dp.baseCalculate()
dp.anlSolution()
dp.numSolution()
print

# Print section
print "Measurement result:"
pr = originalPrint(dp)

pr.xtPrintPrettyTable()
print
pr.solPrintPrettyTable()

print "Dynamic:"
#pr.velPrintSimple()
#pr.engPrintSimple()
#pr.engPrintPrettyTable()
pr.frompPrintPrettyTable()

# Plot section
visio =graths.Visualization(dp)
visio.trajectory() # plot of motion
visio.vFromPfunction()  # velocety-momentum
visio.eFromPfunction() # energy-momentum
