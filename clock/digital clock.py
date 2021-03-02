# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 09:30:30 2020

@author: Gaurav Tyagi
"""
import sys
from tkinter import*
import time

def tick():
    global time1
    time2=time.strftime("%H:%M:%S %p")
    if time2 !=time1:
        time1=time2
        clock.config(text=time2)
    clock.after(1000,tick)

root=Tk()
root.title("Clock")
root.iconbitmap(r"clock.ico")
time1=""
clock=Label(root,font=("Arial Bold",36),bg="red",fg="white")
clock.pack()
tick()
root.mainloop()
