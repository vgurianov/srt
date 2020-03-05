#!/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# Experiment 2: Energy and momentum of a particle
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

    """ Concept = differential equation of particle motion  """

    xa_track = []  # track, analitical solution
    xn_track = []  # track, numerical solution
    pa = []  # momentum, analitical solution
    va = []  # velocity, analitical solution
    vn = []  # velocity, numerical solution
    en = []  # energy, numerical solution

    def __init__(
        self,
        observer,
        particle_velocity,
        size_tick,
        count_tick,
        ):
        ri.DataProcessing.__init__(self, observer, particle_velocity,
                                   size_tick, count_tick)

    def anl_solution(self):
        """ Analytical solution of the motion differential equation  """

        m = float(self.mass) / self.nu_m
        qe = 1 / self.nu_m * (self.nu_t * self.nu_t / self.nu_x) * 1.0 \
            / float(self.size_tick * self.size_tick)
        print 'qE=', qe
        c = self.light_vel
        for i in range(0, len(self.obs.obt_g)):
            ddt = float(self.obs.obt[i] - self.obs.obt[i - 1])
            x = m * c ** 2 / qe * (math.sqrt(1.0 + (qe * self.t[i] / (m
                                   * c)) ** 2) - 1.0)
            self.xa_track.append(x)
            p = qe * self.t[i]
            self.pa.append(p)
            v = p / math.sqrt(m ** 2 + (p / c) ** 2)
            jv = self.t[i] * qe / (m * c)
            v = math.sqrt(jv * jv / (1 + jv * jv)) * c
            self.va.append(v)
        print 'Analytical solution of the differential equation of motion'

    def num_solution(self):
        """ Numerical solution of the motion differential equation
        Euler's method
        
        """

        m = float(self.mass) / self.nu_m
        c = self.light_vel
        p1 = 0.0
        x1 = 0.0
        self.xn_track.append(x1)
        self.vn.append(0.0)
        e = m * c * c
        self.en.append(e)
        for i in range(1, len(self.obs.obt_g)):
            dt = self.t[i] - self.t[i - 1]
            ddt = float(self.obs.obt[i] - self.obs.obt[i - 1])
            qe = 1 / self.nu_m * (self.nu_t * self.nu_t / self.nu_x) \
                * 1.0 / float(self.size_tick * self.size_tick)

            # print "qE=", qe

            p2 = p1 + qe * dt
            self.vn.append(p2 / math.sqrt(m ** 2 + (p2 / c) ** 2))
            e = e + qe * (self.x[i] - self.x[i - 1])
            self.en.append(e)
            v = p2 / math.sqrt(m ** 2 + (p2 / c) ** 2)
            x2 = x1 + v * dt
            self.xn_track.append(x2)
            p1 = p2
            x1 = x2
        print 'Numerical solution of the differential equation of motion'


class OriginalPrint(print_results.TablePrint):

    """ Analytical solution print """

    def __init__(self, dp):
        print_results.TablePrint.__init__(self, dp)

    def sol_print_simple(self):
        print
        print 'Analytical solution'
        for i in self.dt.obs.obt_g:
            print 'Tw=', i, 't =', self.dt.t[i], 'x =', \
                round(self.dt.x[i], 2), 'xa =', \
                round(self.dt.xa_track[i], 2), 'xe =', \
                round(self.dt.xNtrack[i], 2), 'p =', \
                self.dt.momentum_t[i], 'pa=', round(self.dt.pa[i], 2), \
                'v=', round(self.dt.vel_t[i], 2), 'va=', \
                round(self.dt.va[i], 2)

    def sol_print_prettytable(self):
        print
        print 'Analytical (xa, pa, va) and numerical (xe) solution'
        pt = print_results.PrettyTable([
            'Tw',
            't',
            'x',
            'xa',
            'xe',
            'p',
            'pa',
            'v',
            'va',
            ])
        for i in self.dt.obs.obt_g:
            pt.add_row([
                i,
                self.dt.t[i],
                round(self.dt.x[i], 2),
                round(self.dt.xa_track[i], 2),
                round(self.dt.xn_track[i], 2),
                round(self.dt.momentum_t[i], 2),
                round(self.dt.pa[i], 2),
                round(self.dt.vel_t[i], 2),
                round(self.dt.va[i], 2),
                ])
        print pt


class simple_iteraction(mms.Composite):

    """ Concept = Interaction with constant force """

    def __init__(
        self,
        size_tick,
        count_tick,
        particle_velocity,
        observer,
        ):

        # super.__init__(sizeTick, countTick, observer)

        mms.Composite.__init__(self, size_tick, count_tick, observer)
        self.__foo = None

        # particle, initial condition

        self.lst.contents = mms.Leaf(particle_velocity)
        print 'particle_velocity =', particle_velocity
        self.carr = mms.Carrier()
        self.carr.direction = 1

    def interaction(self, car):
        """ Concept = Interaction with big mass """

        if not car is None:
            if car.direction == 0:
                car.direction = 1
            else:
                car.direction = 0
        return car


# Execute ------------------- ------------------------------
# Estimated calculation

c = 2.997925e8  # m/s
lm = 1.0 / c
print 'Estimated calculation for electron:'
m = 9.1e-31  # mass of electron, kg
e = 1.602e-19  # C - Coulomb, e electric charge of electron
nu_m = 1.0 / m
nu_t = 10 * c
f = 1.0 / nu_m * (nu_t / 10.0) * (1.0 / 10.0)
ef = f / e
print 'm= ', m, ' kg, e= ', e, 'C'
print 'nu_m = ', nu_m, 'nu_t = ', nu_t
print 'f=', f, ' N, E=', ef, ' V/m'
tk = m * c / f
d = m * c / f * (math.sqrt(1.0 + f * tk / (m * c) * (f * tk / (m * c)))
                 - 1.0)
print 'z = ', tk, 's ', ' d = ', d, ' m'
print ' must grid ', tk, 'x', d, ' s x m'
print
print 'In c = 1, m =1 system, f =', f / (c * m)
print

# Init parametrs section

particle_velocity = 0  # particle_velocity < sizeTick
size_tick = 10  # size of tact (1 tick)
count_tick = 9  # count of ticks
print 'Parameters:'
print 'count_tick=', count_tick, 'size_tick=', size_tick

# Run section

observer = ri.Table()
xt = simple_iteraction(size_tick, count_tick, particle_velocity,
                       observer)
print
print 'Simulation of particle motion:'
xt.run()
print

# Data processing

print 'Data processing:'
dp = OriginalToolkit(observer, particle_velocity, size_tick, count_tick)
dp.base_calculate()
dp.anl_solution()
dp.num_solution()
print

# Print section

print 'Measurement result:'
pr = OriginalPrint(dp)

pr.xt_print_prettytable()
print
pr.sol_print_prettytable()

print 'Dynamic:'

# pr.velPrintSimple()
# pr.engPrintSimple()
# pr.engPrintPrettyTable()

pr.fromp_print_prettytable()

# Plot section

visio = drawing.Visualization(dp)
visio.trajectory()  # plot of motion
visio.v_from_p_function()  # velocety-momentum
visio.e_from_p_function()  # energy-momentum
