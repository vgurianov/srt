# -*- coding: cp1251 -*-
# Clocks Run Slow modeling

import math

import mmsEx
import ResacherInstruments as ri
import printResult
import graths

class originalToolkit(ri.DataProcessing):
    
    def __init__(self, observer,particle_velosety, sizeTick, countTick):
        #super.__init__(sizeTick, countTick, observer)
        ri.DataProcessing.__init__(self, observer, particle_velosety, sizeTick, countTick)

    # incline calculate
    def incline(self):
        """
        incline k calculate and error
        """
        sgn = 2  # afte point 0.00

        print "It is incline calculate"
        # error k
        dx=[]
        dt=[]
        k_ar = 0.0
        print "Point couple method (d=4)"
        for i in range(0,len(self.obs.obtG)-4,1):
            dx.append(self.obs.obx[i+4]- self.obs.obx[i])
            dt.append(self.obs.obt[i+4]- self.obs.obt[i])
            k_ar1 = float(dt[i])/float(dx[i])
            k_ar = k_ar + k_ar1
            print i, dx[i], dt[i], k_ar1
        k_n = len(dx)
        print "Couple count =", k_n

        k_ar=k_ar/k_n
        print "Measurement incline k_ar=", round(k_ar,sgn)
        dd=0
        for i in range(0, len(dx),1):
            dd1 = (float(dt[i])/float(dx[i])-k_ar)
            dd = dd + dd1*dd1
            
        sk_ar = math.sqrt(dd/(k_n-1)) # standard deviation
        dk_ar = sk_ar/math.sqrt(k_n)  # confidence interval
        print "k_ar =", round(k_ar,sgn), "+/-",round(dk_ar,sgn+1)
        
        # accurate: t'=sqrt(s^2+x^2)= sqrt((x/v)^2+x^2)= x*sqrt(1+1/v^2)
        # x=v*s->s=x/v
        pv = float(self.particle_velosety)/float(self.sizeTick)
        k_an = math.sqrt(1.0+1.0/(pv*pv))
        print "Analytical incline k_an=",round(k_an,sgn), ",k_err%=", round(math.fabs(100*(k_an-k_ar)/k_an),sgn)

# print
class originalPrint(printResult.TablePrint):
    def __init__(self, dp):
        #super.__init__(sizeTick, countTick, observer)
        printResult.TablePrint.__init__(self, dp)

    def xtPrintPrettyTable(self):
        print
        print "Uniform translatory motion of the reference frame"
        pt = printResult.PrettyTable(["Tw","x", "t", "ta", "err%", "tp"])

        for i in self.dt.obs.obtG:
            tp = round(float(self.dt.obs.particleT[i]),1) 
            pt.add_row([i, round(self.dt.x[i],2), self.dt.t[i], round(self.dt.t_acc[i],2), round(self.dt.t_local_err[i],2),tp])   
        print pt



# Inertial reference frame
class irfMotion(mmsEx.Composite):
    __foo = None
    
    def __init__(self, sizeTick, countTick, particle_velocity, observer, frame_velocity):
        #super.__init__(sizeTick, countTick, observer)
        mmsEx.Composite.__init__(self, sizeTick, countTick, observer, frame_velocity)
        self.__foo = None
        # particle, initial condition
        self.lst.contents = mmsEx.Leaf(particle_velocity)
        # print "Particle velocity =",particle_velocity 
        self.carr = None

    def interaction(self, carIn):
        carOut = carIn
        return carOut

        
# Execute -------------------
# Estimated calculation
c = 2.997925e8 # m/s
lm = 1.0/c  # meter of light time
lifetime = 2.6e-8  # seconds (26 nanoseconds)
print "Estimated calculation for Pi+ meson (pion):"
print " lifetime = ", lifetime, "seconds or ",lifetime/lm, " metres of light time"
beta = 0.0
print " beta = v/c = ", beta 
td = lifetime/math.sqrt(1.0 - beta*beta)
print " time dilation = ",td, " seconds or ", td/lm, " metres of light time"
print " distance = ", c*beta*td, "metres"
print
# Init parametrs section
particle_velocity = 0 # particle_velosety < sizeTick
frame_velocity = 5 # 
sizeTick = 10 # size of tick
countTick = 8 # count of ticks
print "Parameters:"
print "countTick=",countTick, "sizeTick=", sizeTick
print "Particle_velocity=",particle_velocity, ",i.e beta = v/c =", float(particle_velocity)/float(sizeTick)
print "Frame_velocity=",frame_velocity, ",i.e beta = v/c =", float(frame_velocity)/float(sizeTick)

# Run section
observer = ri.Table()
xt = irfMotion(sizeTick, countTick, particle_velocity, observer, frame_velocity)
print type(xt)
print
print "Simulation of frame motion:"
xt.run()

# Print section
print
print "Data processing:"
dp = originalToolkit(observer, particle_velocity, sizeTick, countTick)
dp.baseCalculate()
print

print
print "Measurement result:"
pr = originalPrint(dp)
#pr.xtPrintSimple()
pr.xtPrintPrettyTable()

# incline calculation
# dp.incline()
print "Experimental error of measurement t is ", (1.0/float(sizeTick))/2.0

# Plot section
# Graphs
visio =graths.Visualization(dp)
visio.trajectory1() # plot of motion


