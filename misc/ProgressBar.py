# -*- coding: utf-8 -*-
"""
author: Richard Bonye (github Boyne272)
Last updated on Wed Aug 28 08:46:31 2019
"""


import sys
import time as tm
import matplotlib.pyplot as plt


class ProgressBar():
    """
    A simple progress bar for quick and easy user output.

    Call the instance with the iteration number to update the bar.

    Parameters
    ----------

    imax : int
        The number of iterations at which the bar is full

    refresh : int
        The frequency (in iterations) at which the bar should be
        printed. For high iterations with short time per iteration the
        printing of the progress bar can dominate, hence make this number
        high.

    length : int
        The number of characters to fill the bar

    """

    symbol = '#'

    def __init__(self, imax, refresh=1, length=50):

        # store parameters
        self.imax = max(imax - 1, 1) # ensure a value of 1 wil not break it
        self.length = length
        self.refresh = refresh

        # create the time and iteration stores
        self.times = []
        self.iterations = []
        self.start = tm.time()


    def reset(self):
        'reset the time and iteration stores'
        self.times = []
        self.iterations = []
        self.start = tm.time()


    def add_time(self, iteration):
        "store the current time and iteration"
        self.times.append(tm.time()-self.start)
        self.iterations.append(iteration)


    def print_bar(self, i):
        "update the progress bar"
        _m = int(self.length * i/self.imax) + 1
        _n = self.length - _m
        sys.stdout.write("\rProgress |" + ProgressBar.symbol * _m + " " * _n +
                         "| %.4f s" % self.times[-1])


    def __call__(self, i):
        "if on correct iteration update the progress bar and store the time"
        if (i % self.refresh) == 0:
            self.add_time(i)
            self.print_bar(i)
            return True
        return False


    def plot_time(self, axis=None):
        "plot the time vs iterations on the axis if given"

        if axis is None:
            _fig, axis = plt.subplots()

        axis.plot(self.iterations, self.times, '-o')
        axis.set(xlabel="Iteration", ylabel="Time (s)")

        return axis
