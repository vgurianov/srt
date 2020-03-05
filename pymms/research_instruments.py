#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# Measurement and data processing
#
# (C) 2020 Vasyliy I. Gurianov, Russia
# Github: https://github.com/vgurianov/srt
# Released under MIT License
# email: vg2007sns@rambler.ru
# -----------------------------------------------------------

import math


# -----------------------------------------------------------

class Table:

    """ Concept = Data recorder"""

    obt_g = []  # model tick
    obt = []  # time in the rest system
    obx = []  # particle coordinate
    local_t = []  # local time of cell
    particle_t = []  # particle time
    pulse = 0
    pulse_t = []  # interection acts

    def __init__(self):
        pass

    def fix_it(
        self,
        tg,
        tt,
        xx,
        loc_t,
        prt_t,
        ):
        """ x,t - coordinate fixed """

        self.obt_g.append(tg)
        self.obt.append(tt)
        self.obx.append(xx)
        self.local_t.append(loc_t)
        self.particle_t.append(prt_t)

    def detect(self, tg, c):
        """ Force detect """

        if not c is None:
            pulse = 1  # force - we used 1 act of interaction
        else:
            pulse = 0
        self.pulse_t.append(pulse)

    def rewrite_it(
        self,
        tg,
        tt,
        xx,
        loc_t,
        prt_t,
        ):
        """ Rewrite data """

        # pop (i) removes the element with index i and returns it.
        # If you call pop () without parameters, it will be returned
        # and the last element of the list is deleted

        self.obt_g.pop()
        self.obt_g.append(tg)
        self.obt.pop()
        self.obt.append(tt)
        self.obx.pop()
        self.obx.append(xx)
        self.local_t.pop()
        self.local_t.append(loc_t)
        self.particle_t.pop()
        self.particle_t.append(prt_t)

    def data_control(self):
        """ Errors control """

        for i in range(0, self.count_tick):
            if self.obt_g[i] != self.local_t[i]:
                print 'No sync:obtG[i] <> localT[i]: ', i, \
                    self.obt_g[i], self.local_t[i]
            if self.obt_g[i] != self.particle_t[i]:
                print 'No sync:obtG[i] <> particleT[i]: ', i, \
                    self.obt_g[i], self.particle_t[i]


class DataProcessing:

    """ Concept = Data processing """

    obs = None  # primary data table
    particle_velocity = None  # initial velocity of particle
    size_tick = None  # size tick of time
    count_tick = None  # count tick of time
    mass = 1  # mass of particle (natural)
    light_vel = 1.0  # light speed
    nu_t = 0.0  # time coefficient of conversion
    nu_x = 0.0  # length coefficient of conversion
    nu_m = 0.0  # mass coefficient of conversion

    x = []  # particle coordinates
    t = []  # accurate time in the laboratory reference frame
    t_err = []  # time measurement error
    t_acc = []  # analytical magnitude of time
    t_local_err = []  # local error of time (compare with t_acc)

    vel_t = []  # experimental value of velocity
    vel_t_err = []  # experimental error measurement
    vel_anl = []  # analytical velocity as function from momentum

    momentum_t = []  # particle momentum
    eng_t_acc = []  # analytical magnitude of energy
    eng_t = []  # measurement energy
    eng_t_err = []  # energy measurement error
    eng_t_err_sum = []  # energy measurement error in sum

    def __init__(
        self,
        ob,
        v,
        st,
        ct,
        ):
        """
        Parameters:
        -----------
        ob:  primary data table
        v :  initial velocity of particle
        st:  size tick of time
        ct:  count tick of time
        
        """

        self.obs = ob
        self.particle_velocity = v
        self.size_tick = st
        self.count_tick = ct

        # it is define of coefficient of conversion

        self.nu_m = 1.0  # mass coefficient of conversion
        self.nu_t = float(st)  # time coefficient of conversion, 2
        self.nu_x = self.light_vel * self.nu_t  # length coefficient of conversion (then v/c)

        # print "Resalution of model:"

        print 'nu_t =', self.nu_t, ', nu_x =', self.nu_x, ', nu_m =', \
            self.nu_m
        print 'mass =', self.mass, ', light_vel =', self.light_vel
        print ' '

    # base processing

    def xt_calculate(self):
        """ t and x calculate """

        for i in range(0, len(self.obs.obt_g)):
            t = float(self.obs.obt[i]) / self.nu_t
            self.t.append(t)
            self.t_err.append(0.5 * (1.0 / 2.0) / self.nu_t)  # 0.5 is bar
            x = float(self.obs.obx[i]) / self.nu_x
            self.x.append(x)
        print 'coordinate calculated'

    def xt_accurate(self):
        """ accurate t (analytical formula) """

        self.t_acc.append(0.0)
        err = 0.0
        self.t_local_err.append(err)
        for i in range(1, len(self.obs.obt_g)):
            an = math.sqrt(float(self.obs.obt_g[i]) ** 2 + self.x[i]
                           ** 2)
            self.t_acc.append(an)
            err = math.fabs(100.0 * (an - self.t[i]) / an)
            self.t_local_err.append(err)
        print 'accurate coordinate calculated'

    def velocity_calculate(self):
        """ experimental magnitude of velocity """

        self.vel_t.append(0.0)
        self.vel_t_err.append(0.0)
        for i in range(1, len(self.obs.obt_g)):
            dt = float(self.obs.obt[i] - self.obs.obt[i - 1]) \
                / self.nu_x
            dx = float(self.obs.obx[i] - self.obs.obx[i - 1]) \
                / self.nu_x
            vv = dx / dt
            self.vel_t.append(vv)
            vve = self.vel_error_calculate(dt, dx)
            self.vel_t_err.append(vve)
        print 'velocity calculated'

    def vel_error_calculate(self, dt, dx):
        """ experimental error measurement of velocity """

        vv = dx / dt
        del_t = 1.0 / 2.0 / self.nu_t
        del_x = 1.0 / 2.0 / self.nu_x
        varx = 1.0 / dt
        vart = math.fabs(vv) / dt

        # 0.5 to errbar

        vve = 0.5 * math.sqrt(2) * math.sqrt((varx * del_x) ** 2
                + (vart * del_t) ** 2)
        return vve

    def momentum_calculate(self):
        """ momentum """

        p = 0.0
        self.momentum_t.append(p)
        self.vel_anl.append(self.vel_analytical(p))
        for i in range(1, len(self.obs.obt_g)):
            ddt = float(self.obs.obt[i] - self.obs.obt[i - 1])
            dt = self.t[i] - self.t[i - 1]

            # f = (1.0/self.nu_m)*(self.nu_t/float(self.sizeTick))*(float(self.obs.pulseT[i])/(float(self.sizeTick)))

            f = 1.0 / self.nu_m * (1.0 / float(self.size_tick)) \
                * float(self.obs.pulse_t[i])
            dp = f * dt

            # print self.obs.pulse_t[i],f, dp

            p = p + dp
            self.momentum_t.append(p)
            self.vel_anl.append(self.vel_analytical(p))
        print 'momentum calculated'

    def vel_analytical(self, p):
        """ analytical velocity as function from momentum """

        pp = p
        v_anl = pp / math.sqrt(self.mass ** 2 + (pp / self.light_vel)
                               ** 2)
        return v_anl

    # momentum

    def energe_accurate(self):
        """ analytical energy as function from momentum """

        m = float(self.mass) / self.nu_m  # mass
        c = self.light_vel  # light speed
        c = 1.0  # true!
        for i in range(0, len(self.obs.obt_g)):
            p = self.momentum_t[i]
            energy = math.sqrt(m ** 2 * c ** 4 + (p * c) ** 2)
            self.eng_t_acc.append(energy)
        print 'accurate energy calculated'

    # summ error

    def eng_sum_err(self, i):
        """ errror sum """

        se = 0.0
        for i in range(0, i):
            se = se + self.eng_t_err[i] * self.eng_t_err[i]
        se = math.sqrt(se)
        return se

    def energe_calculate(self):
        """ energy measurement  """

        m = float(self.mass) / self.nu_m  # mass
        c = self.light_vel  # light speed
        c = 1.0  # true!
        err_x = 1.0 / 2.0 / self.nu_x  # absolute error of measurement x
        err = 0.0
        self.eng_t_err.append(err)
        self.eng_t_err_sum.append(0.0)
        energy = m * c ** 2
        self.eng_t.append(energy)
        for i in range(1, len(self.obs.obt_g)):
            ddt = float(self.obs.obt[i] - self.obs.obt[i - 1])
            dt = self.t[i] - self.t[i - 1]
            f = 1.0 / self.nu_m * (self.nu_t / float(self.size_tick)) \
                * (float(self.obs.pulse_t[i]) / float(self.size_tick))
            dx = self.x[i] - self.x[i - 1]
            dA = f * dx  # i.e. force multiple by displacement
            energy = energy + dA
            self.eng_t.append(energy)
            err = err_x * math.sqrt(2.0 * f)
            self.eng_t_err.append(err)
            self.eng_t_err_sum.append(0.5 * self.eng_sum_err(i))  # , where 0.5 to errbar
        print 'energy calculated'

    def base_calculate(self):
        """ obligatory caculation """

        self.xt_calculate()
        self.xt_accurate()
        self.velocity_calculate()
        self.momentum_calculate()
        self.energe_calculate()
        self.energe_accurate()
