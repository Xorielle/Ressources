#! /usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk 


Num_Vertical = ("\nA\nB\nC\nD\nE\nF\nG\nH\nI\nJ\nK\nL\nM\nN\nO\nP\nQ\nR\nS\nT\nU\nV\nW\nX\nY\nZ") 
Num_Horizontal = ("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z") 

window = tk.Tk() 
window.geometry("1200x700") 

SVBar = tk.Scrollbar(window) 
SVBar.pack (side = tk.RIGHT, 
			fill = "y") 

SHBar = tk.Scrollbar(window, 
					orient = tk.HORIZONTAL) 
SHBar.pack (side = tk.BOTTOM, 
			fill = "x") 

TBox = tk.Text(window, 
			height = 500, 
			width = 500, 
			yscrollcommand = SVBar.set, 
			xscrollcommand = SHBar.set, 
			wrap = "none") 

TBox = tk.Text(window, 
			height = 500, 
			width = 500, 
			yscrollcommand = SVBar.set, 
			xscrollcommand = SHBar.set, 
			wrap = "none") 

TBox.pack(expand = 0, fill = tk.BOTH) 

TBox.insert(tk.END, Num_Horizontal) 
TBox.insert(tk.END, Num_Vertical) 

SHBar.config(command = TBox.xview) 
SVBar.config(command = TBox.yview) 

window.mainloop() 
