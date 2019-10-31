# -*- coding: utf-8 -*-
"""
Playing with pythons GUI interfaces

author: Richard Bonye (github Boyne272)
Last updated on Thu Sep 12 14:06:30 2019
"""


import tkinter as tk
import matplotlib
import skimage as ski
import numpy as np

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class FirstGUI():
    
    def __init__(self, master=None, title='Example GUI'):
        
        # setup
        master = master if master is not None else tk.Tk()
        self.master = master

        # add name
        master.title(title)

        # set dimensions
#        master.geometry('1000x500+300+300')
        

    def __call__(self):
        self.master.mainloop()


#    def click_canvas(self):
#        self.canvas = tk.Canvas(self.master, width=100, height=100)
#        f = lambda event : print('Clicked at', event.x, event.y)
#        self.canvas.bind('<Button-1>', f)
#        self.canvas.pack()


    def img_canvas(self, img):
        
        # setup the figure
        fig = Figure(dpi=100)
        self.ax = fig.add_axes([0.01, 0.01, 0.99, 0.99])
        self.ax.imshow(img)
        self.ax.axis('off')
        
        # create canvas object
        fig_canvas = FigureCanvasTkAgg(fig, self.master)
        self.canvas = fig_canvas.get_tk_widget()

        # create the click event on the mpl figure
        self.points = []
        def put_point(event):
#            print('Clicked at', event.xdata, event.ydata)
            x, y = event.xdata, event.ydata
            if x is None or event.key!='p':
                return
            self.ax.plot(x, y, '*')
            self.points.append([x, y])
            fig.canvas.draw()
        fig.canvas.mpl_connect('key_press_event', put_point)
 
       
        def connect_points(event):
            self.ax.clear()
            x, y = np.array(self.points).T
            y = img.shape[0] - y
            self.ax.plot(x, y, 'r-')
            self.ax.set(xlim=[0, img.shape[1]], ylim=[0, img.shape[0]])
            fig.canvas.draw()
            
        def add_image(event):
            self.ax.clear()
            self.ax.imshow(img)
            self.ax.axis('off')
            fig.canvas.draw()
        
        self.canvas.bind('<r>', add_image)
        self.canvas.bind('<d>', connect_points)
        
        # create the two buttons
        self.connect_points = tk.Button(self.master, command=connect_points)
        self.reset = tk.Button(self.master, command=add_image)
        
        # create the tool bar
        toolbar = NavigationToolbar2Tk(fig_canvas, self.master)
        toolbar.update()
        
        # add these to the figure
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        

if __name__ == '__main__':
    gui = FirstGUI()
#    img = ski.io.imread('such_data_very_science.jpg')
    img = ski.io.imread('kevin.jpg')
    gui.img_canvas(img)
    gui()
    