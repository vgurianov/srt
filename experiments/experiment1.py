# -*- coding: cp1251 -*-
# Clocks Run Slow modeling

import math

import mms
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
        print "pair points method (d=4)"
        for i in range(0,len(self.obs.obtG)-4,1):
            dx.append(self.obs.obx[i+4]- self.obs.obx[i])
            dt.append(self.obs.obt[i+4]- self.obs.obt[i])
            k_ar1 = float(dt[i])/float(dx[i])
            k_ar = k_ar + k_ar1
            print i, dx[i], dt[i], k_ar1
        k_n = len(dx)
        print "Point count =", k_n

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
        print "Trajectory of particle and time particle"
        pt = printResult.PrettyTable(["Tw","x", "t", "ta", "err%", "tp"])

        for i in self.dt.obs.obtG:
            tp = round(float(self.dt.obs.particleT[i]),1) 
            pt.add_row([i, round(self.dt.x[i],2), self.dt.t[i], round(self.dt.t_acc[i],2), round(self.dt.t_local_err[i],2),tp])   
        print pt




class freeMotion(mms.Composite):
    __foo = None
    
    def __init__(self, sizeTick, countTick, particle_velosety, observer):
        #super.__init__(sizeTick, countTick, observer)
        mms.Composite.__init__(self, sizeTick, countTick, observer)
        self.__foo = None
        # particle, initial condition
        self.lst.contents = mms.Leaf(particle_velosety)
        print "Particle velosety =",particle_velosety 
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
beta = 0.5
print " beta = v/c = ", beta 
td = lifetime/math.sqrt(1.0 - beta*beta)
print " time dilation = ",td, " seconds or ", td/lm, " metres of light time"
print " distance = ", c*beta*td, "metres"
print
# Init parametrs section
particle_velosety = 2 # particle_velosety < sizeTick
sizeTick = 10 # size of tick
countTick = 7 # count of ticks
print "Parameters:"
print "countTick=",countTick, "sizeTick=", sizeTick
print "Particle_velosety=",particle_velosety, ",i.e beta = v/c =", float(particle_velosety)/float(sizeTick)

# Run section
observer = ri.Table()
#xt= mms.Composite(sizeTick, countTick, particle_velosety, observer)
xt = freeMotion(sizeTick, countTick, particle_velosety, observer)
print type(xt)
print
print "Simulation of particle motion:"
xt.run()

# Print section
print
print "Data processing:"
dp = originalToolkit(observer, particle_velosety, sizeTick, countTick)
dp.baseCalculate()
print

print
print "Measurement result:"
pr = originalPrint(dp)
#pr.xtPrintSimple()
pr.xtPrintPrettyTable()

# incline calculation
dp.incline()

# Plot section
# Graphs
print "Experimental error of measurement t is ", (1.0/float(sizeTick))/2.0
visio =graths.Visualization(dp)
visio.trajectory1() # plot of motion

