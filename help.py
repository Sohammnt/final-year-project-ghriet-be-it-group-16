# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 14:37:36 2021

@author: Harshada Garule
"""
import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os
import cv2

window = tk.Tk()
window.geometry("800x600")
window.title("Help")

image2 = Image.open('2.png')
image2 = image2.resize((800, 600), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) 
window.mainloop()