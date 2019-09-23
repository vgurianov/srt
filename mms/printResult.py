# -*- coding: cp1251 -*-
from external.prettytable import PrettyTable
import math




class TablePrint:
    dt = None

    def __init__(self, dat):
        self.dt = dat

    # coordinates print
    def xtPrintSimple(self):
        print
        print "Trajectory of particle and local time"
        for i in self.dt.obs.obtG:
            print "Tw=",i,"x =",self.dt.x[i], "t=", self.dt.t[i], "Accurate t=",round(self.dt.t_acc[i],2), "err%=", round(self.dt.t_local_err[i],2)

    def xtPrintPrettyTable(self):
        print
        print "Trajectory of particle and local time"
        pt = PrettyTable()
        pt = PrettyTable(["Tw","x", "t", "ta", "err%"])

        for i in self.dt.obs.obtG:
            pt.add_row([i, round(self.dt.x[i],2), self.dt.t[i], round(self.dt.t_acc[i],2), round(self.dt.t_local_err[i],2) ])   
        print pt

    # velocity print
    def velPrintSimple(self):
        print
        print "Velocity of particle"
        for i in self.dt.obs.obtG:
            if self.dt.velAnl[i] == 0.0:
                err = 0.0
            else:
                err = math.fabs(100.0*(self.dt.vel_t[i]-self.dt.velAnl[i])/self.dt.velAnl[i])
            print "Tw=",i,"p =",round(self.dt.momentum_t[i],2), "v=", round(self.dt.vel_t[i],2), "Analytical v=",round(self.dt.velAnl[i],2), "err%=", round(err,2)


    # energy print
    def engPrintSimple(self):
        print
        print "Energy of particle as function from momentum"
        for i in self.dt.obs.obtG:
            err = math.fabs(100.0*(self.dt.eng_t[i]-self.dt.eng_t_acc[i])/self.dt.eng_t_acc[i])
            print "Tw=",i,"p =",self.dt.momentum_t[i], "E=", round(self.dt.eng_t[i],2), "Analytical E=",round(self.dt.eng_t_acc[i],2), "err%=", round(err,2)

    # velocity and energy print
    def frompPrintPrettyTable(self):
        print
        print "Velocity end energy of particle as function from momentum"
        pt = PrettyTable()
        pt = PrettyTable(["Tw","p", "v", "va", "v,err%", "E", "Ea", "E,err%"])
        for i in self.dt.obs.obtG:
            if self.dt.velAnl[i] == 0.0:
                err1 = 0.0
            else:
                err1 = math.fabs(100.0*(self.dt.vel_t[i]-self.dt.velAnl[i])/self.dt.velAnl[i])
            err2 = math.fabs(100.0*(self.dt.eng_t[i]-self.dt.eng_t_acc[i])/self.dt.eng_t_acc[i])
 
            pt.add_row([i, round(self.dt.momentum_t[i],2), round(self.dt.vel_t[i],2), round(self.dt.velAnl[i],2), round(err1,2), round(self.dt.eng_t[i],2), round(self.dt.eng_t_acc[i],2), round(err2,2) ])   
        print pt

