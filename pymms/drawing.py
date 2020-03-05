#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# Graphic output
#
# (C) 2020 Vasyliy I. Gurianov, Russia
# Github: https://github.com/vgurianov/srt
# Released under MIT License
# email: vg2007sns@rambler.ru
# -----------------------------------------------------------

import math
import matplotlib.pyplot as plt
import matplotlib.ticker
import pylab


# -----------------------------------------------------------

class Visualization:

    """ Data plots """

    dt = []  # Data table

    def __init__(self, dat):
        """ Parameters: dat is the data table. """

        self.dt = dat

    def trajectory(self):
        """ Track """

        ltrackt = []  # light
        for i in range(self.dt.count_tick):
            ltrackt.append(self.dt.light_vel * self.dt.t[i])

        # plots:

        (fig, ax) = plt.subplots()

        # x-t data

        ax.plot(
            self.dt.x,
            self.dt.t,
            marker='o',
            linestyle=' ',
            color='black',
            label='result of measurements',
            )

        # analytical solution:

        ax.plot(self.dt.xa_track, self.dt.t, linestyle='-', color='red'
                , label='continuum')
        ax.plot(
            self.dt.xn_track,
            self.dt.t,
            marker='x',
            linestyle='--',
            color='blue',
            label="Euler's method",
            )

        # ax.plot(self.self.dt.x, an, linestyle=":", color="green", label="accurate")

        ax.plot(ltrackt, self.dt.t, linestyle='-', color='yellow',
                label='s=0 (light)')

        # error

        ax.errorbar(self.dt.x, self.dt.t, fmt='k ', yerr=self.dt.t_err)

        # signature on the horizontal x-axis

        ax.set_xlabel('x')
        xm = -1.0
        for i in range(len(self.dt.x)):
            if self.dt.x[i] > xm:
                xm = self.dt.x[i]
        stepx = round(xm / float(len(self.dt.x)), 1)
        xm = round(xm + stepx, 1)
        ax.set_xlim([0.0, xm])

        # signature on vertical y axis

        ax.set_ylabel('t')
        ym = -1.0
        for i in range(len(self.dt.t)):
            if self.dt.t[i] > ym:
                ym = self.dt.t[i]
        stepy = round(ym / float(len(self.dt.t)), 1)
        ym = round(ym + stepy, 1)
        ax.set_ylim([0.0, ym])

        # Create an instance of the class that will be responsible for the location of the labels (base is step on x)

        locatorx = matplotlib.ticker.MultipleLocator(base=stepx)

        # Set the locator for the main labels

        ax.xaxis.set_major_locator(locatorx)

        # Create an instance of the class that will be responsible for the location of the labels (base is step on y)

        locatory = matplotlib.ticker.MultipleLocator(base=stepy)

        # Set the locator for the main labels

        ax.yaxis.set_major_locator(locatory)

        ax.grid()

        # show legend

        ax.legend(loc='upper left')

        # show drawing

        plt.show()

    def trajectory1(self):
        """ Track and curve s**2 + x**2 = t**2 """

        trackt = []  # particle trajectory,
        trackx = []  # particle trajectory
        an = []  # analitical s**2 + x**2 = t**2
        s1 = []  # s = 10; s = 0, light
        s2 = []  # s = 20;
        s3 = []  # s = 40;
        for i in range(0, len(self.dt.obs.obt_g)):
            trackt.append(float(i))
            trackx.append(self.dt.x[i])
            an.append(math.sqrt(float(i) ** 2 + self.dt.x[i] ** 2))
            s1.append(math.sqrt(1.0 ** 2 + self.dt.x[i] ** 2))
            s2.append(math.sqrt(2.0 ** 2 + self.dt.x[i] ** 2))
            s3.append(math.sqrt(4.0 ** 2 + self.dt.x[i] ** 2))

        # plots:

        (fig, ax) = plt.subplots()  # figsize=(7,5)

        # trajectory

        ax.plot(
            trackx,
            trackt,
            marker='+',
            linewidth=1,
            linestyle='-',
            color='green',
            label='treck',
            )

        # measurement t
        # ax.plot(self.dt.x, self.dt.t, marker="+", linestyle=" ", color="blue", label="result of measurement")

        ax.plot(
            self.dt.x,
            self.dt.t,
            marker='o',
            linestyle=' ',
            color='black',
            label='result of measurement',
            )

        # analitical t

        ax.plot(self.dt.x, an, linestyle='-', color='red',
                label='continuum')

        # light trajectory

        ax.plot(trackx, trackx, linestyle='-', color='yellow',
                label='s=0 (light)')

        # s(x) curves

        ax.plot(
            trackx,
            s1,
            linestyle=':',
            linewidth=1,
            color='k',
            label='s=1.0',
            )
        ax.plot(
            trackx,
            s2,
            linestyle=':',
            linewidth=1,
            color='k',
            label='s=2.0',
            )
        ax.plot(
            trackx,
            s3,
            linestyle=':',
            linewidth=1,
            color='k',
            label='s=4.0',
            )

        # error of measurement t

        ax.errorbar(self.dt.x, self.dt.t, fmt='k ', yerr=self.dt.t_err)

        # signature on the horizontal x-axis

        ax.set_xlabel('x in metres')
        xm = -1.0
        for i in range(len(self.dt.x)):
            if self.dt.x[i] > xm:
                xm = self.dt.x[i]
        stepx = round(xm / float(len(self.dt.x)), 1)
        xm = round(xm + stepx, 1)
        ax.set_xlim([0.0, xm])

        # signature on vertical y axis

        ax.set_ylabel('t in metres of light time ')
        ym = -1.0
        for i in range(len(self.dt.t)):
            if self.dt.t[i] > ym:
                ym = self.dt.t[i]
        stepy = round(ym / float(len(self.dt.t)), 1)
        ym = round(ym + stepy, 1)
        ax.set_ylim([0.0, ym])

        # Create an instance of the class that will be responsible for the location of the labels (base is step on x)

        locatorx = matplotlib.ticker.MultipleLocator(base=stepx)

        # Set the locator for the main labels

        ax.xaxis.set_major_locator(locatorx)

        # Create an instance of the class that will be responsible for the location of the labels (base is step on y)

        locatory = matplotlib.ticker.MultipleLocator(base=stepy)

        # Set the locator for the main labels

        ax.yaxis.set_major_locator(locatory)

        ax.grid()

        # show legend

        ax.legend(loc='upper left')

        # show drawing

        plt.show()

    def v_from_p_function(self):
        """ Velocity as function from momentum. """

        track_c = []  # p classical function,
        for i in range(len(self.dt.momentum_t)):
            track_c.append(self.dt.momentum_t[i] / self.dt.mass)

        (fig, ax) = plt.subplots()

        ax.plot(
            self.dt.momentum_t,
            track_c,
            linestyle=':',
            linewidth=1,
            color='b',
            label='classic',
            )

        # marker="+", markersize = 13,
        # ax.plot(self.dt.momentum_t, self.observer.velT,  linestyle=" ",
        #        color="k",marker="+", markersize = 13,   label="measurement")

        ax.plot(
            self.dt.momentum_t,
            self.dt.vel_t,
            linestyle=' ',
            color='k',
            marker='o',
            label='result of measurements',
            )
        ax.plot(
            self.dt.momentum_t,
            self.dt.vel_anl,
            linestyle='-',
            color='red',
            linewidth=1,
            label='continuum',
            )

        # Euler's method == analitical function. We not plot it.

        ax.plot(
            self.dt.momentum_t,
            self.dt.vn,
            linestyle='--',
            color='blue',
            marker='x',
            linewidth=1,
            label="Euler's method",
            )

        # error

        ax.errorbar(self.dt.momentum_t, self.dt.vel_t, fmt='k ',
                    yerr=self.dt.vel_t_err)

        xm = -1.0
        for i in range(len(self.dt.momentum_t)):
            if self.dt.momentum_t[i] > xm:
                xm = self.dt.momentum_t[i]
        stepx = round(xm / float(len(self.dt.momentum_t)), 1)
        xm = round(xm + stepx, 1)
        ax.set_xlim([0, xm])  # xm = 0.85

        # signature on the horizontal x-axis

        ax.set_xlabel('p')

        # Create an instance of the class that will be responsible for the location of the labels (base is step on x)

        locatorx = matplotlib.ticker.MultipleLocator(base=stepx)  # step on x is base=0.1

        # Set the locator for the main labels

        ax.xaxis.set_major_locator(locatorx)

        # line draw

        line = matplotlib.lines.Line2D([0.0, 9.0], [1.0, 1.0], color='b'
                )
        ax.add_line(line)
        plt.text(0.7, 1.01, u'light speed', horizontalalignment='center'
                 )
        ax.set_ylim([0, 1.1])

        # signature on vertical y axis

        ax.set_ylabel('v')

        # Create an instance of the class that will be responsible for the location of the labels (base is step on y)

        locatory = matplotlib.ticker.MultipleLocator(base=0.1)  # step on y is base=0.1

        # Set the locator for the main labels

        ax.yaxis.set_major_locator(locatory)

        ax.grid()

        # show legend

        ax.legend(loc='upper left')

        # show drawing
        # pylab.show()

        plt.show()

    def e_from_p_function(self):
        """ Energy as function from momentum """

        (fig, ax) = plt.subplots()
        ax.plot(
            self.dt.momentum_t,
            self.dt.eng_t,
            marker='o',
            linestyle=' ',
            color='black',
            label='result of measurements',
            )
        ax.plot(self.dt.momentum_t, self.dt.eng_t_acc, linestyle='-',
                color='red', label='continuum')
        ax.plot(
            self.dt.momentum_t,
            self.dt.en,
            linestyle='--',
            marker='x',
            color='blue',
            label="Euler's method",
            )

        # error

        ax.errorbar(self.dt.momentum_t, self.dt.eng_t, fmt='k ',
                    yerr=self.dt.eng_t_err_sum)

        xm = -1.0
        for i in range(len(self.dt.momentum_t)):
            if self.dt.momentum_t[i] > xm:
                xm = self.dt.momentum_t[i]
        stepx = round(xm / float(len(self.dt.momentum_t)), 1)
        xm = round(xm + stepx, 1)
        ax.set_xlim([0, xm])  # 0.85

        # signature on the horizontal x-axis

        ax.set_xlabel('p')

        # Create an instance of the class that will be responsible for the location of the labels (base is step on x)

        locatorx = matplotlib.ticker.MultipleLocator(base=stepx)  # stepx$ step on x is base=0.1

        # Set the locator for the main labels

        ax.xaxis.set_major_locator(locatorx)

        ym = -1.0
        y0 = self.dt.mass
        for i in range(len(self.dt.eng_t)):
            if self.dt.eng_t[i] > ym:
                ym = self.dt.eng_t[i]
        stepy = round((ym - y0) / float(len(self.dt.eng_t)), 2)

        # print ym, stepy

        ym = round(ym + stepy, 2)
        ax.set_ylim([y0 - stepy, ym])  # 0.9, 1.4

        # signature on vertical y axis

        ax.set_ylabel('E')

        # Create an instance of the class that will be responsible for the location of the labels (base is step on y)

        locatory = matplotlib.ticker.MultipleLocator(base=stepy)  # stepy $ step on y is base=0.05

        # Set the locator for the main labels

        ax.yaxis.set_major_locator(locatory)
        ax.grid()

        # show legend

        ax.legend(loc='upper left')

        # show drawing

        plt.show()
