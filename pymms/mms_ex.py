#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# Advanced mms module: uniform translatory motion of a reference frame
#
# (C) 2020 Vasyliy I. Gurianov, Russia
# Github: https://github.com/vgurianov/srt
# Released under MIT License
# email: vg2007sns@rambler.ru
# -----------------------------------------------------------

import math


# -----------------------------------------------------------

class Carrier:

    direction = None


class Jump:

    direction = None
    next = None


class Leaf:

    tick = -1
    head_of_jump = None
    current_of_jump = None

    def __init__(self, v):
        if v <= 0:
            self.head_of_jump = None
        else:

            self.head_of_jump = Jump()
            self.current_of_jump = self.headOfJump
            for i in range(1, v):
                self.current_of_jump.next = Jump()
                self.current_of_jump = self.current_of_jump.next

        # self.currentOfJump = self.headOfJump  # active

        self.current_of_jump = None  # non active

    def is_active(self):
        if self.current_of_jump is None:
            return False
        else:
            return True

    def jumpp(self):
        if not self.current_of_jump is None:
            self.current_of_jump = self.current_of_jump.next

    def run(self):
        self.tick = self.tick + 1
        print 'Particle tick=:', self.tick

    def reset(self):

        # self.tick = -1

        if not self.current_of_jump is None:
            print "Particle isn't stop"
        self.current_of_jump = self.head_of_jump

    def do_impact(self, car):
        if not car is None:
            if self.head_of_jump is None:
                self.head_of_jump = Jump()
            else:
                jj = Jump()
                jj.next = self.head_of_jump
                self.head_of_jump = jj

            # self.current_of_jump = self.head_of_jump

    def interaction(self, car):
        if not car is None:
            if car.direction == 0:
                car.direction = 1
            else:
                car.direction = 0
        return car


class Temp:

    next = None
    t = -1
    marked = None
    dedicated_node = False

    def __init__(self, t):
        self.t = t  # time stamp for measurement


class ListItem:

    x = 0
    left = None
    right = None
    contents = None
    tmp = None
    count_tmp = 0
    temp = None
    _err_flag = False  # error indicator
    observer = None  # observer in everyone cell

    def __init__(self, x, o):
        self.x = x
        self.observer = o

    def app_temp(self, tm):
        self.count_tmp = self.count_tmp + 1
        if self.temp is None:
            self.temp = Temp(self.count_tmp - 1)  # t = count_tmp-1
            self.tmp = self.temp
        else:
            self.tmp.next = Temp(self.count_tmp - 1)
            self.tmp = self.tmp.next

        self.tmp.marked = tm

    def one_jump(self):
        if self.contents.is_active():
            self.contents.jumpp()
            self.right.contents = self.contents
            self.contents = None

    def item_run(
        self,
        tt,
        t_glob,
        c,
        ):
        if not self.tmp is None:

            # print "1/All ListItem is act:","for tt=", tt.t, "ListItem=", self.x, "marked=", self.tmp.marked.t

            if tt == self.tmp.marked:

                # print "2/All ListItem is act:","for tt=", tt.t, "ListItem=", self.x, "tloc=", self.tmp.t

                if not self.contents is None:
                    if self.contents.is_active():
                        self.one_jump()
                    else:

                        # if not _err_flag:

                        print 'ListItem is act:', 'for tt=marked=', \
                            tt.t, 'ListItem=', self.x, 'tloc=', \
                            self.tmp.t
                        self.contents.run()
                        self.observer.fix_it(t_glob, tt.t, self.x,
                                tt.t, self.contents.tick)
                        self.key = True

                        # else:
                            # self.observer.rewriteIt(tGlob, tt.t, self.x, tt.t, self.contents.tick)
                            # print ",and ListItem is act:","for tt=marked=", tt.t, "ListItem=", self.x, "tloc=", self.tmp.t

                        self.contents.do_impact(c)
                        self.observer.detect(t_glob, c)

                self.tmp = self.tmp.next

    def reset_tmp(self):
        self.tmp = self.temp


class Composite:

    """
    """

    tmp = None  # time
    lst = None  # space
    carr = None  # interaction carrier

    tick = 0  # counter time

    s_tick = None  # size tact
    s_vel = None  # frame velocity
    frame_velocity = 0

    def __init__(
        self,
        size_tick,
        count_tick,
        observer,
        frame_vel,
        ):

        # self.carr = Carrier()

        # Resolution tact of time i.e. tick

        self.s_tick = Jump()
        csv = self.s_tick
        for i in range(1, size_tick):
            csv.next = Jump()
            csv = csv.next

        # Frame velocity

        self.frame_velocity = frame_vel
        if self.frame_velocity <= 0:
            self.s_vel = None
        else:
            if size_tick - self.frame_velocity < 0:
                print 'Warning: frame_velocity > size_tick'
            self.s_vel = self.s_tick
            for i in range(1, size_tick - self.frame_velocity + 1):
                self.s_vel = self.s_vel.next

        # Space & time

        self.lst = ListItem(0, observer)
        ll = self.lst
        self.tmp = Temp(0)
        tt = self.tmp
        ii = 1
        for k in range(0, count_tick, 1):
            tt.dedicated_node = True
            for i in range(0, size_tick, 1):
                ll.right = ListItem(ii, observer)
                tt.next = Temp(ii)
                leftll = ll
                ll = ll.right
                ll.left = leftll
                tt = tt.next
                ii = ii + 1

        size = ii - 1
        print 'Laboratory time count =', size

        # print " "

        sh = 0
        tt = self.tmp
        while not tt is None:
            if tt.dedicated_node:
                s = tt.t
                ll = self.lst
                while not ll is None:
                    t = math.trunc(math.ceil(math.sqrt(s ** 2 + (sh
                                   - ll.x) ** 2)))
                    if t < size:
                        st = self.tmp
                        for i in range(0, t, 1):
                            st = st.next
                        ll.app_temp(st)

                        # print "s=",s,", t=",t, "ListItem=",ll.x, "mark=", st.t  #marking debug

                    ll = ll.right
                sh = sh + self.frame_velocity

            tt = tt.next

        ll = self.lst
        while not ll is None:

            # print ll.x, ll.count_tmp, ll.temp.t,ll.temp.marked.t

            ll.reset_tmp()  # do begin
            ll = ll.right

        # print " "

        # particle
        # self.lst.contents = Leaf(particle_velocity)
        # print "Particle velocity =",particle_velocity

    # Don't use, it is classic motion, it is example.

    def move(self):
        ll = self.lst
        while not ll is None:
            if not ll.contents is None:
                ll.contents.reset()

            ll = ll.right

        # motion of particle

        ll = self.lst
        while not ll is None:
            if not ll.contents is None:
                if ll.contents.is_activity():

                    # place control
                    # print "Particle in ",ll.x

                    ll.contents.jumpp()
                    ll.right.contents = ll.contents
                    ll.contents = None
            ll = ll.right

    # New motion of particle.

    def move_reset(self):
        ll = self.lst
        while not ll is None:
            if not ll.contents is None:
                if not ll._err_flag:
                    print 'Sync error: Particle reset but cell=', ll.x, \
                        ' not sync'
                ll.contents.reset()
            ll = ll.left

    def interaction(self, car_in):
        car_out = None
        return car_out

    def run(self):

        # t=0 is singular point

        tt = self.tmp
        ll = self.lst
        car = self.interaction(self.carr)
        ll.item_run(tt, self.tick, car)
        tt = tt.next
        sv = None

        # run of local time

        while not tt is None:

            if tt.dedicated_node:
                self.tick = self.tick + 1
                print 'Time of laboratory clock Tw=', self.tick
                self.move_reset()
                car = self.interaction(self.carr)
                sv = self.s_vel
                while not sv is None:
                    self.lst = self.lst.right
                    sv = sv.next

            # else:

            # space move
            # if not (sV is None):
            #    self.lst = self.lst.right
            #    sV = sV.next
            # else:

            ll = self.lst
            ll.x = 0
            while not ll is None:
                ll = ll.left
                if not ll is None:
                    ll.x = ll.right.x + 1

            ll = self.lst
            while not ll is None:
                ll.item_run(tt, self.tick, car)
                ll = ll.left

            tt = tt.next
