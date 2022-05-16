import sqlite3
import tkinter  as tk
from tkinter import *
import time
import numpy as np

import tkinter.messagebox

import os
from PIL import Image , ImageTk
from PIL import *
from PIL import Image 
 

root = tk.Tk()
root.geometry('700x500')
root.title("Login Form")
root.resizable(False,False)

Name=StringVar()
upass=StringVar()


#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")
import sqlite3
my_conn = sqlite3.connect('evaluation.db')


image2 =Image.open('common.png')
image2 =image2.resize((700,500), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image
background_label.place(x=0, y=0)
#-----------------------------------



def login_now():
   
##### tkinter window ######
    print("reg")
 
   
 
    from subprocess import call
    call(["python", "GUI_Master.py"])  
   
   




label_1 = Label(root, text="User Name",width=20,font=("bold", 11),bg="white", fg="black")
label_1.place(x=130,y=160)

entry_1 = Entry(root,textvar=Name,bg="lightgray",font=("bold", 11))
entry_1.place(x=400,y=160)

label_2 = Label(root, text="Password",width=20,font=("bold", 11),bg="white", fg="black")
label_2.place(x=130,y=210)

entry_2 = Entry(root,textvar=upass,bg="lightgray",font=("bold", 11))
entry_2.place(x=400,y=210)


Button(root, text='Login Now',width=20,bg='white',fg='black',command=login_now).place(x=250,y=270)



root.mainloop()



