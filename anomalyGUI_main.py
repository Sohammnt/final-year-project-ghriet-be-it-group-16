# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter.ttk import * 
from time import strftime
from tkinter import*
from tkinter import ttk, LEFT, END
from tkinter import Menu
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time


global fn
fn = ""
##############################################+=============================================================

root = tk.Tk()
root.configure(background="")





w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Intelligent Video Surveillance System")

def reg():
    from subprocess import call
    call(["python","anomaly_registration.py"])

def log():
    from subprocess import call
    call(["python","anomaly_login.py"])
    
def gue():
    from subprocess import call
    call(["python","GUI_Master.py"])
    
def con():
    from subprocess import call
    call(["python","contact.py"])
    
def ab():
    from subprocess import call
    call(["python","about.py"])
    

    
menubar = Menu(root)
file = Menu(menubar, tearoff = 0)
file1 = Menu(menubar, tearoff = 0)
file2 = Menu(menubar, tearoff = 0)

menubar.add_cascade(label ='Get Access', menu = file)
file.add_command(label ='Login', command = log)
file.add_command(label ='Register', command = reg)
file.add_command(label ='Guest', command = gue)

menubar.add_cascade(label ='Contact ', menu = file1)
file1.add_command(label ='Contact Us', command = con)

menubar.add_cascade(label ='About', menu = file2)
file2.add_command(label ='Team', command = ab)




image2 = Image.open('1.png')
image2 = image2.resize((1360, 678), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

    
def window():
  root.destroy()
  




root.config(menu = menubar)

root.mainloop()