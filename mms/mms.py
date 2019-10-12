# -*- coding: cp1251 -*-
import math

# --------------------------------------
class Carrier:
    direction = None

class Jump:
    direction = None
    next = None

class Leaf:
    tick = -1;
    headOfJump = None
    currentOfJump = None

    def __init__(self, v):
        if v<=0:
            self.headOfJump = None
            
        else:
            self.headOfJump = Jump()
            self.currentOfJump = self.headOfJump
            for i in range(1,v):
                self.currentOfJump.next = Jump()
                self.currentOfJump = self.currentOfJump.next
            
        # self.currentOfJump = self.headOfJump  # active
        self.currentOfJump = None   # non active
        
    def isActivity(self):
        if self.currentOfJump is None:
            return False
        else:
            return True
        
    def jumpp(self):
        if not (self.currentOfJump is None):
            self.currentOfJump = self.currentOfJump.next

    def run(self):
        self.tick = self.tick+1
        print "Particle tick=:", self.tick
    
    def reset(self):
        #self.tick = -1
        self.currentOfJump = self.headOfJump

    """
        Interaction
    """
    def doImpact(self, car):
        if not (car is None):
            if self.headOfJump is None:
                self.headOfJump = Jump()
            else:
                jj = Jump()
                jj.next = self.headOfJump
                self.headOfJump = jj
            self.currentOfJump = self.headOfJump

    def interaction(self,car):
        if not (car is None):
            if car.direction == 0:
                car.direction = 1
            else:
                car.direction = 0
        return car
    
class Temp:
    next = None
    t = -1
    marked = None
    lb = False
    
    def __init__(self, t):
        self.t = t # time stamp for measurement

class ListItem:
    x = None
    left = None
    right = None
    contents = None
    tmp = None
    countTmp = 0
    temp = None
    key = False   # ? error indicator
    observer = None  # observer in everyone cell

    def __init__(self, x, o):
        self.x = x
        self.observer = o

    def appTemp(self, tm):
        self.countTmp = self.countTmp + 1
        if self.temp is None:
            self.temp = Temp(self.countTmp-1) # t = countTmp-1
            self.tmp = self.temp
        else:
            self.tmp.next = Temp(self.countTmp-1)
            self.tmp = self.tmp.next
            
        self.tmp.marked = tm

    def oneJump(self):
        if self.contents.isActivity():
            self.contents.jumpp()
            self.right.contents = self.contents
            self.contents = None

    def ItemRun(self, tt, tGlob, c):
        if not (self.tmp is None):
            if tt == self.tmp.marked:
                #print "All ListItem is act:","for tt=", tt.t, "ListItem=", self.x, "tloc=", self.tmp.t
                if not (self.contents is None):
                    if self.contents.isActivity():
                        self.oneJump()
                    else:
                        if not self.key:
                            self.contents.run()
                            self.observer.fixIt(tGlob, tt.t, self.x, tt.t, self.contents.tick)
                            print "ListItem is act:","for tt=marked=", tt.t, "ListItem=", self.x, "tloc=", self.tmp.t
                            self.key = True
                        else:
                            self.observer.rewriteIt(tGlob, tt.t, self.x, tt.t, self.contents.tick)
                            print ",and ListItem is act:","for tt=marked=", tt.t, "ListItem=", self.x, "tloc=", self.tmp.t

                        self.contents.doImpact(c)
                        self.observer.detect(tGlob, c)
                            
                self.tmp = self.tmp.next
               

    def resetTmp(self):
        self.tmp = self.temp
    
class Composite:
    """
    """
    tmp = None  # time
    lst = None  # space
    carr = None   # interaction carrier

    tick = 0     # counter time


    def __init__(self, sizeTick, countTick, observer):

        #self.carr = Carrier()

        # Space & time
        self.lst = ListItem(0, observer)
        ll = self.lst
        self.tmp = Temp(0)
        tt = self.tmp
        ii = 1
        for k in range(0, countTick, 1):
            tt.lb = True
            for i in range(0,sizeTick,1):
                ll.right = ListItem(ii,observer)
                tt.next = Temp(ii)
                ll = ll.right
                tt = tt.next
                ii = ii+1

        size = ii-1        
        print "Time count =", size            
        #print " "

        tt = self.tmp
        while not (tt is None):
            if tt.lb:
                ll = self.lst
                while not (ll is None):
                    s = math.trunc(math.ceil(math.sqrt(tt.t**2+ll.x**2)))
                    if s < size:
                        st = self.tmp
                        for i in range(0,s,1):
                            st=st.next
                        ll.appTemp(st)
                        # print "s=",s,"ListItem=",ll.x, "mark=", st.t  #marking debug
                    ll = ll.right
            tt = tt.next
            
        ll = self.lst
        while not (ll is None):
            #print ll.x, ll.countTmp, ll.temp.t,ll.temp.marked.t
            ll.resetTmp()  # do begin
            ll = ll.right
        #print " "

        # particle
        #self.lst.contents = Leaf(particle_velosety)
        #print "Particle velosety =",particle_velosety 

    def move(self):   # don't use
        ll = self.lst
        while not (ll is None):
            if not (ll.contents is None):
                ll.contents.reset()
                
            ll = ll.right

        # motion of particle 
        ll = self.lst
        while not (ll is None):
            if not (ll.contents is None):
                if ll.contents.isActivity():
                    # place control
                    #print "Particle in ",ll.x
                    ll.contents.jumpp()
                    ll.right.contents = ll.contents
                    ll.contents = None
            ll = ll.right

    def moveReset(self):
        ll = self.lst
        while not (ll is None):
            if not (ll.contents is None):
                ll.contents.reset()
            ll = ll.right
            
        
    def interaction(self, carIn):
        carOut = None
        return carOut

    def run(self):
        
        # t=0 is singular point
        tt = self.tmp
        ll = self.lst
        car = self.interaction(self.carr);
        ll.ItemRun(tt,self.tick,car)
        tt = tt.next
        
        # run of local time    
        while not (tt is None):
            
            if tt.lb:
                self.tick = self.tick + 1
                print "World time =", self.tick
                #self.move()
                self.moveReset()
                #car = Carrier()
                car = self.interaction(self.carr);
            #else:
                
            ll = self.lst
            while not (ll is None):
                ll.ItemRun(tt,self.tick, car)
                ll = ll.right
                
             
                    
            tt = tt.next

