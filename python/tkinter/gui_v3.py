# -*- coding: utf-8 -*-
"""
author: Richard Bonye (github Boyne272)
Last updated on Fri Sep 13 09:43:51 2019
"""


import tkinter as tk
from tkinter import ttk


class gui():
    def __init__(self, master=None):
        
        # initalise tk obj (aka. master)
        master = tk.Tk() if master is None else master
        self.master = master
        
        # master settings
        master.title('Example Tabs')
        master.geometry('500x280+300+300')
        
        # create tabs
        self.tab_parent = ttk.Notebook(master)
        
        self.page_one = first_page(self.tab_parent)
        self.tab_parent.add(self.page_one, text='first page')
        
        self.page_two = ttk.Frame(self.tab_parent)
        self.tab_parent.add(self.page_two, text='second page')
        
        self.tab_parent.pack(expand=1, fill='both')
        
        # start gui
        master.mainloop()


class first_page(ttk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)
        
        # === WIDGETS FOR TAB ONE
        firstLabelTabOne = tk.Label(self, text="First Name:")
        familyLabelTabOne = tk.Label(self, text="Family Name:")
        jobLabelTabOne = tk.Label(self, text="Job Title:")
        
        firstEntryTabOne = tk.Entry(self)
        familyEntryTabOne = tk.Entry(self)
        jobEntryTabOne = tk.Entry(self)
        
        imgLabelTabOne = tk.Label(self)
        
        buttonForward = tk.Button(self, text="Forward")
        buttonBack = tk.Button(self, text="Back")
        
        # === ADD WIDGETS TO GRID ON TAB ONE
        firstLabelTabOne.grid(row=0, column=0, padx=15, pady=15)
        firstEntryTabOne.grid(row=0, column=1, padx=15, pady=15)
        
        familyLabelTabOne.grid(row=1, column=0, padx=15, pady=15)
        familyEntryTabOne.grid(row=1, column=1, padx=15, pady=15)
        
        jobLabelTabOne.grid(row=2, column=0, padx=15, pady=15)
        jobEntryTabOne.grid(row=2, column=1, padx=15, pady=15)
        
        imgLabelTabOne.grid(row=0, column=2, rowspan=3, padx=15, pady=15)
        
        buttonBack.grid(row=3, column=0,  padx=15, pady=15)
        buttonForward.grid(row=3, column=2,  padx=15, pady=15)
        
        parent.pack(expand=1, fill='both')



if __name__ == '__main__':
    menu = gui()