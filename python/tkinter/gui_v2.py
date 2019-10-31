# -*- coding: utf-8 -*-
"""
author: Richard Bonye (github Boyne272)
Last updated on Fri Sep 13 09:25:25 2019
"""


import tkinter as tk


# setup the form
form = tk.Tk()
form.title('Example Tabs')
form.geometry('500x280+300+300')

# create the tab objs
tab_parent = tk.ttk.Notebook(form)
tab1 = tk.ttk.Frame(tab_parent)
tab2 = tk.ttk.Frame(tab_parent)

# link them
tab_parent.add(tab1, text='first page')
tab_parent.add(tab2, text='second page')
tab_parent.pack(expand=1, fill='both')

# open window
form.mainloop()