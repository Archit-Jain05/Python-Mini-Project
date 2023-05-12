import tkinter as tk
from tkinter import Button,Label
import Main
from Main import *


def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()


def screen_two():
    clear_frame()
    button_2 = Button(window, text="Go to  screen one", command=lambda: screen_one())
    button_2.pack(pady=10)
    label_2 = Label(window, text="Label on window two")
    label_2.pack(pady=10)


def screen_one():
    clear_frame()
    Login.__init__()
    Regredirect=tk.Button(rootlog)
    Regredirect["bg"] = "#f0f0f0"
    Regredirect["borderwidth"] = "0px"
    ft = tkFont.Font(family='Times',size=10)
    Regredirect["font"] = ft
    Regredirect["fg"] = "#0038ff"
    Regredirect["justify"] = "center"
    Regredirect["text"] = "Dont have an Account? Sign up here."
    Regredirect["relief"] = "flat"
    Regredirect.place(x=330,y=350,width=250,height=30)
    Regredirect["command"] = rootlog.Regredirectbtn
    rootlog.mainloop()


screen_one()
