#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# Main module of package pymms
#
# (C) 2020 Vasyliy I. Gurianov, Russia
# Github: https://github.com/vgurianov/srt
# Released under MIT License
# email: vg2007sns@rambler.ru
# -----------------------------------------------------------

import math


# -----------------------------------------------------------

class Carrier:

    """ Concept = Interaction carrier """

    direction = None


class Jump:

    """ Concept = Stock of movement """

    direction = None
    next = None


class Leaf:

    """ Concept = Particle """

    tick = -1  # Concept = The clock of particle
    head_of_jump = None  # Concept = Stock of particle movement
    current_jump = None

    def __init__(self, v):
        """ Parameters: v is velocity of a particle """

        # Create linked list head_of_jump.

        if v <= 0:
            self.head_of_jump = None
        else:

            self.head_of_jump = Jump()
            self.current_jump = self.head_of_jump
            for i in range(1, v):
                self.current_jump.next = Jump()
                self.current_jump = self.current_jump.next

        # self.current_jump = self.head_of_jump  # active

        self.current_jump = None  # non active

    def is_active(self):
        if self.current_jump is None:
            return False
        else:
            return True

    def jumpp(self):
        """ Concept = Particle has jump in space """

        if not self.current_jump is None:
            self.current_jump = self.current_jump.next

    def run(self):
        """ Concept = Run of particle time """

        self.tick = self.tick + 1
        print 'Particle tick=:', self.tick

    def reset(self):

        # Go to head of list current_jump .
        # self.tick = -1

        if not self.current_jump is None:
            print "Particle isn't stop"
        self.current_jump = self.head_of_jump

    def do_impact(self, car):
        """ Concept = Force impact  to particle """

        if car is not None:
            if self.head_of_jump is None:
                self.head_of_jump = Jump()
            else:
                jj = Jump()
                jj.next = self.head_of_jump
                self.head_of_jump = jj

            # self.current_jump = self.head_of_jump

    def interaction(self, car):
        """ Concept = The particle impact to the interaction carrier """

        if car is not None:
            if car.direction == 0:
                car.direction = 1
            else:
                car.direction = 0
        return car


class Temp:

    """ Concept = Time interval """

    next = None  # It is next node of linked list
    t = -1  # Concept = Local clock
    marker = None  # Concept = Marker of time
    dedicated_node = False  # Concept = Dedicated (bearing) node

    def __init__(self, t):
        self.t = t  # It is timestamp for measurement.


class ListItem:

    """ Concept = Space cell """

    x = None  # Concept = Coordinates
    left = None  # Concept = Left link
    right = None  # Concept = Right link
    contents = None  # Concept = Cell contents
    tmp = None  # Linked list. Concept = Local time
    count_tmp = 0  # Length list tmp
    temp = None  # Head of list tmp
    observer = None  # Concept = Observer in everyone cell
    _err_flag = False  # Error indicator

    def __init__(self, x, o):
        self.x = x
        self.observer = o

    def app_temp(self, tm):
        """ Append node to the list tmp. """

        self.count_tmp = self.count_tmp + 1
        if self.temp is None:
            self.temp = Temp(self.count_tmp - 1)  # t = count_tmp-1
            self.tmp = self.temp
        else:
            self.tmp.next = Temp(self.count_tmp - 1)
            self.tmp = self.tmp.next

        self.tmp.marker = tm

    def one_jump(self):
        """ Concept = One jump of particle """

        if self.contents.is_active():
            self.contents.jumpp()
            self.right.contents = self.contents
            self.contents = None

    def item_run(
        self,
        tt, # current time moment
        t_glob, # current tick
        c, # interaction carrier
        ):
        """ Concept = One step local time of the cell """

        if not self.tmp is None:

            # print "1/All ListItem is act:","for tt=", tt.t, "ListItem=", self.x, "marker=", self.tmp.marker.t

            if tt == self.tmp.marker:

                # print "2/All list_item is act:","for tt=", tt.t, "list_item=", self.x, "tloc=", self.tmp.t

                if not self.contents is None:
                    if self.contents.is_active():
                        self.one_jump()
                    else:
                        if not self._err_flag:
                            print 'Cell has act:', 'for tt=marker=', \
                                tt.t, 'cell=', self.x, 'tloc=', \
                                self.tmp.t
                            self.contents.run()
                            self.observer.fix_it(t_glob, tt.t, self.x,
                                    tt.t, self.contents.tick)
                            self._err_flag = True
                        else:
                            self.observer.rewrite_it(t_glob, tt.t,
                                    self.x, tt.t, self.contents.tick)
                            print ',and cell has act:', \
                                'for tt=marker=', tt.t, 'cell=', \
                                self.x, 'tloc=', self.tmp.t

                        self.contents.do_impact(c)
                        self.observer.detect(t_glob, c)

                self.tmp = self.tmp.next

    def reset_tmp(self):

        # Go to head of list tmp.

        self.tmp = self.temp


class Composite:

    """ Concept = The physical spacetime
    """

    tmp = None  # Concept = Time
    lst = None  # Concept = Space
    carr = None  # Concept = Interaction carrier

    tick = 0  # Concept = Clock of laboratory time

    def __init__(
        self,
        size_tick, 
        count_tick,
        observer,
        ):
        """
        Parameters:
        -----------
        size_tick:  time tick size 
        count_tick: ticks count
        observer:   detector
        
        """

        # self.carr = Carrier()

        # Create of space & time.

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
                ll = ll.right
                tt = tt.next
                ii = ii + 1

        size = ii - 1
        print 'Laboratory time size =', size

        # print " "

        # Marking local time for cells.

        tt = self.tmp
        while not tt is None:
            if tt.dedicated_node:
                s = tt.t
                ll = self.lst
                while not ll is None:
                    t = math.trunc(math.ceil(math.sqrt(s ** 2 + ll.x
                                   ** 2)))
                    if t < size:
                        st = self.tmp
                        for i in range(0, t, 1):
                            st = st.next
                        ll.app_temp(st)

                        # print "s=",s,"item=",ll.x, "marker=", st.t  #marking debug

                    ll = ll.right
            tt = tt.next

        ll = self.lst
        while not ll is None:

            # print ll.x, ll.count_tmp, ll.temp.t,ll.temp.marker.t

            ll.reset_tmp()  # go to begin list tmp
            ll = ll.right

        # print " "

        # particle
        # self.lst.contents = Leaf(particle_velosety)
        # print "Particle velosety =",particle_velosety

    def move(self):

    # Don't use, it is classic motion, it is example.

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

    def move_reset(self):

    # New motion of particle.

        ll = self.lst
        while not ll is None:
            if not ll.contents is None:
                if not ll._err_flag:
                    print 'Sync error: Particle reset but in cell=', \
                        ll.x, ' particle time not sync'
                ll.contents.reset()
            ll = ll.right

    def interaction(self, car_in):

    # Concept = Interaction
    # It is interaction with the big mass in laboratory

        car_out = None
        return car_out

    def run(self):
        """ Concept = Exist of spacetime  """

        # t=0 is singular point

        print 'Time of laboratory clock Tw =', self.tick
        tt = self.tmp
        ll = self.lst
        car = self.interaction(self.carr)
        ll.item_run(tt, self.tick, car)
        tt = tt.next

        # run of local time

        while not tt is None:

            if tt.dedicated_node:
                self.tick = self.tick + 1
                print 'Time of laboratory clock Tw =', self.tick

                # self.move() # It is classical motion of particle (example).

                self.move_reset()
                car = self.interaction(self.carr)

            ll = self.lst
            while not ll is None:
                ll.item_run(tt, self.tick, car)
                ll = ll.right

            tt = tt.next

    def runtest(self):
        #print "Test mms"
        return "Test mms"
