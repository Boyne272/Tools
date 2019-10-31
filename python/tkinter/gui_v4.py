# -*- coding: utf-8 -*-
"""
author: Richard Bonye (github Boyne272)
Last updated on Fri Sep 13 11:33:39 2019
"""


# imports 
import matplotlib
import skimage as ski
import tkinter as tk
from tkinter import ttk


# matplotlib settings 
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
# WARNING above will not work in idle. must be called from terminal


class gui():
    def __init__(self, master=None):
        
        # initalise tk obj (aka. master)
        master = tk.Tk() if master is None else master
        self.master = master
        
        # master settings
        master.title('Image and Tabs')
        master.geometry('1000x500+300+300')
        
        # create image side
        self.left = ttk.Frame(master)
        img_obj1 = image(self.left)
        img_obj1.show_img(ski.io.imread('kevin.jpg'))
        
        # create settings side
        self.right = ttk.Frame(master)
        self.tab_parent = ttk.Notebook(self.right)
        
        self.tab_one = ttk.Frame(self.tab_parent)
        self.tab_parent.add(self.tab_one, text='first page')
        self.tab_two = ttk.Frame(self.tab_parent)
        self.tab_parent.add(self.tab_two, text='second page')
        
        self.tab_parent.pack(fill='both', expand=True)
        
        # pack and start the main window
        self.left.pack(side=tk.LEFT, expand=1, fill='both')
        self.right.pack(side=tk.RIGHT, expand=1, fill='both')
        master.mainloop()


class image():
    def __init__(self, parent):
        
        self.parent = parent
        
        # setup the figure
        self.fig = Figure(dpi=100)
        self.ax = self.fig.add_axes([0.01, 0.01, 0.99, 0.99])
        self.ax.axis('off')
        
         # create canvas object
        fig_canvas = FigureCanvasTkAgg(self.fig, self.parent)
        self.canvas = fig_canvas.get_tk_widget()
        
        # create the tool bar
        self.toolbar = NavigationToolbar2Tk(fig_canvas, self.parent)
        self.toolbar.update()
        
        self.canvas.pack(fill='both', expand=True)
        
        
    def show_img(self, img):
        self.ax.imshow(img)
        self.fig.canvas.draw()
        
    
    def add_function(self, event, func):
        # add function to canvas event
        self.fig.canvas.mpl_connect(event, func)


if __name__ == '__main__':
    menu = gui()