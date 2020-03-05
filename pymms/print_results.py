#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# Data output to print
#
# (C) 2020 Vasyliy I. Gurianov, Russia
# Github: https://github.com/vgurianov/srt
# Released under MIT License
# email: vg2007sns@rambler.ru
# -----------------------------------------------------------

import math
import prettytable


# -----------------------------------------------------------

class TablePrint:

    """ Print data is as table. """

    dt = None

    def __init__(self, dat):
        """ Parameters: dat is data table. """

        self.dt = dat

    def xt_print_simple(self):

        # coordinates print

        print
        print 'Trajectory of particle and local time'
        for i in self.dt.obs.obtG:
            print 'Tlab=', i, 'x =', self.dt.x[i], 't=', self.dt.t[i], \
                'Accurate t=', round(self.dt.t_acc[i], 2), 'err%=', \
                round(self.dt.t_local_err[i], 2)

    def xt_print_prettytable(self):

        # coordinates print

        print
        print 'Trajectory of particle and local time'
        pt = prettytable.PrettyTable()
        pt = prettytable.PrettyTable(['Tlab', 'x', 't', 'ta', 'err%'])

        for i in self.dt.obs.obt_g:
            pt.add_row([i, round(self.dt.x[i], 2), self.dt.t[i],
                       round(self.dt.t_acc[i], 2),
                       round(self.dt.t_local_err[i], 2)])
        print pt

    def vel_print_simple(self):

        # velocity print

        print
        print 'Velocity of particle'
        for i in self.dt.obs.obt_g:
            if self.dt.vel_anl[i] == 0.0:
                err = 0.0
            else:
                err = math.fabs(100.0 * (self.dt.vel_t[i]
                                - self.dt.vel_anl[i])
                                / self.dt.vel_anl[i])
            print 'Tlab=', i, 'p =', round(self.dt.momentum_t[i], 2), \
                'v=', round(self.dt.vel_t[i], 2), 'Analytical v=', \
                round(self.dt.vel_anl[i], 2), 'err%=', round(err, 2)

    def eng_print_simple(self):

        # energy print

        print
        print 'Energy of particle as function from momentum'
        for i in self.dt.obs.obt_g:
            err = math.fabs(100.0 * (self.dt.eng_t[i]
                            - self.dt.eng_t_acc[i])
                            / self.dt.eng_t_acc[i])
            print 'Tlab=', i, 'p =', self.dt.momentum_t[i], 'E=', \
                round(self.dt.eng_t[i], 2), 'Analytical E=', \
                round(self.dt.eng_t_acc[i], 2), 'err%=', round(err, 2)

    def fromp_print_prettytable(self):

        # velocity and energy print

        print
        print 'Velocity end energy of particle as function from momentum'
        pt = prettytable.PrettyTable()
        pt = prettytable.PrettyTable([
            'Tlab',
            'p',
            'v',
            'va',
            'v,err%',
            'E',
            'Ea',
            'E,err%',
            ])
        for i in self.dt.obs.obt_g:
            if self.dt.vel_anl[i] == 0.0:
                err1 = 0.0
            else:
                err1 = math.fabs(100.0 * (self.dt.vel_t[i]
                                 - self.dt.vel_anl[i])
                                 / self.dt.vel_anl[i])
            err2 = math.fabs(100.0 * (self.dt.eng_t[i]
                             - self.dt.eng_t_acc[i])
                             / self.dt.eng_t_acc[i])

            pt.add_row([
                i,
                round(self.dt.momentum_t[i], 2),
                round(self.dt.vel_t[i], 2),
                round(self.dt.vel_anl[i], 2),
                round(err1, 2),
                round(self.dt.eng_t[i], 2),
                round(self.dt.eng_t_acc[i], 2),
                round(err2, 2),
                ])
        print pt
