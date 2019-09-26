# -*- coding: cp1251 -*-

import math
import matplotlib.pyplot as plt
import matplotlib.ticker
import pylab


class Visualization:
    dt = []

    def __init__(self, d):
        self.dt = d


    # Track
    def trajectory(self):
        ltrackt = []  # light 
        for i in range(self.dt.countTick):
            ltrackt.append(self.dt.lightVel*self.dt.t[i])

        fig, ax = plt.subplots()
        # функция y1(x), синий, надпись y(x)
        #ax.plot(trackx, trackt, marker="+",linestyle="-", color="red", label="treck")
        ax.plot(self.dt.x, self.dt.t, marker="o", linestyle=" ", color="black", label="result of measurements")
        # it is analytical solution:
        ax.plot(self.dt.xAtrack, self.dt.t,  linestyle="-", color="red", label="analitical curve")
        ax.plot(self.dt.xNtrack, self.dt.t, marker="x", linestyle="--", color="blue", label="Euler method")
        #ax.plot(self.self.dt.x, an, linestyle=":", color="green", label="accurate")
        ax.plot(ltrackt, self.dt.t, linestyle="-", color="yellow", label="s=0 (light)")

        # error
        ax.errorbar(self.dt.x, self.dt.t,fmt='k ',yerr=self.dt.t_err)

        # подпись у горизонтальной оси х
        ax.set_xlabel("x")
        xm = -1.0
        for i in range(len(self.dt.x)):
            if self.dt.x[i]>xm:
                xm = self.dt.x[i]
        stepx = round(xm/float(len(self.dt.x)), 1)
        xm = round(xm+stepx,1)        
        ax.set_xlim ([0.0, xm])
        # подпись у вертикальной оси y
        ax.set_ylabel("t")
        ym = -1.0
        for i in range(len(self.dt.t)):
            if self.dt.t[i]>ym:
                ym = self.dt.t[i]
        stepy = round(ym/float(len(self.dt.t)),1)
        ym = round(ym+stepy,1)        
        ax.set_ylim ([0.0, ym])
        # Создаем форматер x.xxx
        #formatter = matplotlib.ticker.FormatStrFormatter ("%.1f")
        # Установка форматера для оси Y
        #ax.yaxis.set_major_formatter (formatter)
        
        # Создаем экземпляр класса, который будет отвечать за расположение меток (base is step on x)
        locatorx = matplotlib.ticker.MultipleLocator (base=stepx)
        # Установим локатор для главных меток
        ax.xaxis.set_major_locator(locatorx)
        # Создаем экземпляр класса, который будет отвечать за расположение меток (base is step on y)
        locatory = matplotlib.ticker.MultipleLocator (base=stepy)
        # Установим локатор для главных меток
        ax.yaxis.set_major_locator(locatory)


        ax.grid()
        # показывать условные обозначения
        ax.legend(loc='upper left')
        #показать рисунок
        plt.show()

    # Track and curve s**2 + x**2 = t**2
    def trajectory1(self):
        trackt = []  # particle trajectory, 
        trackx = []  # particle trajectory
        an = [] # analitic s**2 + x**2 = t**2
        s1 = []  # s = 10; s = 0, light
        s2 = []  # s = 20;
        s3 = []  # s = 40;
        for i in range(0,len(self.dt.obs.obtG)):
            trackt.append(float(i))
            trackx.append(self.dt.x[i])
            an.append(math.sqrt(float(i)**2+self.dt.x[i]**2))
            s1.append(math.sqrt(1.0**2+self.dt.x[i]**2))
            s2.append(math.sqrt(2.0**2+self.dt.x[i]**2))
            s3.append(math.sqrt(4.0**2+self.dt.x[i]**2))

        fig, ax = plt.subplots()
        # 
        ax.plot(trackx, trackt, marker="+",linewidth = 1, linestyle="-", color="red", label="treck")
        ax.plot(self.dt.x, self.dt.t, marker="+", linewidth = 1, linestyle=" ", color="blue", label="result of measurement")
        ax.plot(self.dt.x, an, linestyle=":", linewidth = 1, color="green", label="accurate")
        ax.plot(trackx, trackx, linestyle="-",linewidth = 1, color="yellow", label="s=0 (light)")
        ax.plot(trackx, s1, linestyle=":", linewidth = 1, color="k", label="s=1.0")
        ax.plot(trackx, s2, linestyle=":", linewidth = 1, color="k", label="s=2.0")
        ax.plot(trackx, s3, linestyle=":", linewidth = 1, color="k", label="s=4.0")

        # error
        #ax.errorbar(self.dt.x, self.dt.t,fmt='k ',yerr=self.dt.t_err)

        # signature on the horizontal x-axis
        ax.set_xlabel("x in metres")
        xm = -1.0
        for i in range(len(self.dt.x)):
            if self.dt.x[i]>xm:
                xm = self.dt.x[i]
        stepx = round(xm/float(len(self.dt.x)), 1)
        xm = round(xm+stepx,1)        
        ax.set_xlim ([0.0, xm])
        # signature on vertical y axis
        ax.set_ylabel("t in metres of light time ")
        ym = -1.0
        for i in range(len(self.dt.t)):
            if self.dt.t[i]>ym:
                ym = self.dt.t[i]
        stepy = round(ym/float(len(self.dt.t)),1)
        ym = round(ym+stepy,1)        
        ax.set_ylim ([0.0, ym])
        
        # Create an instance of the class that will be responsible for the location of the labels (base is step on x)
        locatorx = matplotlib.ticker.MultipleLocator (base=stepx)
        # Set the locator for the main labels
        ax.xaxis.set_major_locator(locatorx)
        # Create an instance of the class that will be responsible for the location of the labels (base is step on y)
        locatory = matplotlib.ticker.MultipleLocator (base=stepy)
        # Set the locator for the main labels
        ax.yaxis.set_major_locator(locatory)

        ax.grid()
        # show legend
        ax.legend(loc='upper left')
        # show drawing
        plt.show()

    # Velocity as function from momentum
    def vFromPfunction(self):
        trackC = []  # p classical function, 
        for i in range(len(self.dt.momentum_t)):
            trackC.append(self.dt.momentum_t[i]/self.dt.mass)

        fig, ax = plt.subplots()


        # функция y1(x), синий, надпись y(x)
        ax.plot(self.dt.momentum_t, trackC, linestyle=":",linewidth = 1,
                color="b", label="classic")
        #marker="+", markersize = 13,
        #ax.plot(self.dt.momentum_t, self.observer.velT,  linestyle=" ", 
        #        color="k",marker="+", markersize = 13,   label="measurement")
        ax.plot(self.dt.momentum_t, self.dt.vel_t,  linestyle=" ", 
                color="k",marker="o",   label="result of measurements")
        ax.plot(self.dt.momentum_t, self.dt.velAnl, linestyle="-", color="red",
                linewidth = 1, label="accurate value")
        ax.plot(self.dt.momentum_t, self.dt.vN, linestyle="--", color="blue",
                marker="x", linewidth = 1, label="Euler method")

        # error
        ax.errorbar(self.dt.momentum_t, self.dt.vel_t,fmt='k ',yerr=self.dt.vel_t_err)


        xm = -1.0
        for i in range(len(self.dt.momentum_t)):
            if self.dt.momentum_t[i]>xm:
                xm = self.dt.momentum_t[i]
        stepx = round(xm/float(len(self.dt.momentum_t)), 1)
        xm = round(xm+stepx,1)        
        ax.set_xlim ([0, xm])   # xm = 0.85
        # подпись у горизонтальной оси х
        ax.set_xlabel("p")
        # Создаем экземпляр класса, который будет отвечать за расположение меток
        locatorx = matplotlib.ticker.MultipleLocator (base=stepx)  # step on x is base=0.1
        # Установим локатор для главных меток
        ax.xaxis.set_major_locator(locatorx)

        # line draw 
        line = matplotlib.lines.Line2D ([0.0, 9.0], [1.0, 1.0], color="b")
        ax.add_line (line)
        plt.text(0.6, 1.01, u"light speed", horizontalalignment="center")
        ax.set_ylim ([0, 1.1])

        # подпись у вертикальной оси y
        ax.set_ylabel("v")
        # Создаем экземпляр класса, который будет отвечать за расположение меток
        locatory = matplotlib.ticker.MultipleLocator (base=0.1) # step on y is base=0.1
        # Установим локатор для главных меток
        ax.yaxis.set_major_locator(locatory)

        ax.grid()
        # показывать условные обозначения
        ax.legend(loc='upper left')
        #показать рисунок
        #pylab.show()
        plt.show()


    # Energy as function from momentum   
    def eFromPfunction(self):

        fig, ax = plt.subplots()
        # функция y1(x), синий, надпись y(x)
        ax.plot(self.dt.momentum_t, self.dt.eng_t, marker="o", linestyle=" ", color="black", label="result of measurements")
        ax.plot(self.dt.momentum_t, self.dt.eng_t_acc, linestyle="-", color="red", label="analitycal curve")
        ax.plot(self.dt.momentum_t, self.dt.eN, linestyle="--",marker="x", color="blue", label="Euler method")
        # error
        ax.errorbar(self.dt.momentum_t, self.dt.eng_t,fmt='k ',yerr=self.dt.eng_t_err_sum)

        xm = -1.0
        for i in range(len(self.dt.momentum_t)):
            if self.dt.momentum_t[i]>xm:
                xm = self.dt.momentum_t[i]
        stepx = round(xm/float(len(self.dt.momentum_t)), 1)
        xm = round(xm+stepx,1)        
        ax.set_xlim ([0, xm])  # 0.85
        # подпись у горизонтальной оси х
        ax.set_xlabel("p")
        # Создаем экземпляр класса, который будет отвечать за расположение меток
        locatorx = matplotlib.ticker.MultipleLocator (base=stepx)  # stepx$ step on x is base=0.1
        # Установим локатор для главных меток
        ax.xaxis.set_major_locator(locatorx)

        ym = -1.0
        y0 = self.dt.mass
        for i in range(len(self.dt.eng_t)):
            if self.dt.eng_t[i]>ym:
                ym = self.dt.eng_t[i]
        stepy = round((ym-y0)/float(len(self.dt.eng_t)), 2)
        #print ym, stepy
        ym = round(ym + stepy, 2)        
        ax.set_ylim ([y0-stepy, ym])  # 0.9, 1.4
        # подпись у вертикальной оси y
        ax.set_ylabel("E")
        # Создаем экземпляр класса, который будет отвечать за расположение меток
        locatory = matplotlib.ticker.MultipleLocator (base=stepy)  #stepy $ step on y is base=0.05
        # Установим локатор для главных меток
        ax.yaxis.set_major_locator(locatory)
        ax.grid()
        # показывать условные обозначения
        ax.legend(loc='upper left')
        #показать рисунок
        plt.show()

