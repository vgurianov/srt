# -----------------------------------------------------------
# Experiment 1: Time dilation
# ver. 1.0 (2020.01.10)
#
# (C) 2020 Vasyliy I. Gurianov, Russia
# Released under MIT License
# github:  https://github.com/vgurianov/srt
# email:   vg2007sns@rambler.ru
# -----------------------------------------------------------

import math
import mms
import research_instruments as ri
import print_results
import drawing
# -----------------------------------------------------------

class OriginalToolkit(ri.DataProcessing):
    """ Concept = Incline calculate  """   
    def __init__(self, observer,particle_velocity, size_tick, count_tick):
        ri.DataProcessing.__init__(self, observer, particle_velocity, size_tick, count_tick)
        """
        Parameters:
        -----------
        observer:   detector
        particle_velocity: particle velocity
        size_tick:  time tick size 
        count_tick: ticks count
        
        """

    def incline(self):
        """ Incline k calculate and error """
        sgn = 2  # afte point 0.00

        print "It is incline calculate"
        # error k
        dx=[]
        dt=[]
        k_ar = 0.0
        print "Point couple method (d=4)"
        for i in range(0,len(self.obs.obt_g)-4,1):
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
        pv = float(self.particle_velocity)/float(self.size_tick)
        k_an = math.sqrt(1.0+1.0/(pv*pv))
        print "Analytical incline k_an=",round(k_an,sgn), ",k_err%=", round(math.fabs(100*(k_an-k_ar)/k_an),sgn)

class OriginalPrint(print_results.TablePrint):
    """ Data print. """
    def __init__(self, dp):
        print_results.TablePrint.__init__(self, dp)

    def xt_print_prettytable(self):
        print
        print "Trajectory of particle and time particle"
        pt = print_results.PrettyTable(["Tw","x", "t", "ta", "err%", "tp"])

        for i in self.dt.obs.obt_g:
            tp = round(float(self.dt.obs.particle_t[i]),1) 
            pt.add_row([i, round(self.dt.x[i],2), self.dt.t[i], round(self.dt.t_acc[i],2), round(self.dt.t_local_err[i],2),tp])   
        print pt




class FreeMotion(mms.Composite):
    """ Concept = Free motion of particle """
    
    def __init__(self, size_tick, count_tick, particle_velocity, observer):
        mms.Composite.__init__(self, size_tick, count_tick, observer)
        """
        Parameters:
        -----------
        size_tick:  time tick size 
        count_tick: ticks count
        particle_velocity: particle velocity
        observer:   detector
        
        """
        # particle, initial condition
        self.lst.contents = mms.Leaf(particle_velocity)
        print "Particle velocity = ",particle_velocity 
        self.carr = None

    def interaction(self, car_in):
        # Concept = Interaction    
        # no interaction   
        car_out = car_in
        return car_out

# Execute ---------------------------------------------------

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
particle_velocity = 3 # particle_velosety < sizeTick
size_tick = 10 # size of tick
count_tick = 8 # count of ticks
print "Parameters:"
print "count_tick=",count_tick, "size_tick=", size_tick
print "particle_velocity=",particle_velocity, ",i.e beta = v/c =", float(particle_velocity)/float(size_tick)

# Run section
observer = ri.Table()
#xt= mms.Composite(sizeTick, countTick, particle_velosety, observer)
xt = FreeMotion(size_tick, count_tick, particle_velocity, observer)
print
print "Simulation of particle motion:"
xt.run()

# Print section
print
print "Data processing:"
dp = OriginalToolkit(observer, particle_velocity, size_tick, count_tick)
dp.base_calculate()
print

print
print "Measurement result:"
pr = OriginalPrint(dp)
#pr.xtPrintSimple()
pr.xt_print_prettytable()

# incline calculation
dp.incline()
print "Experimental error of measurement t is ", (1.0/float(size_tick))/2.0

# Plot section
# Graphs
visio =drawing.Visualization(dp)
visio.trajectory1() # plot of motion


