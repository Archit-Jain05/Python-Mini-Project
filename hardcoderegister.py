import tkinter as tk
from tkinter import *

class Login:
    def __init__(self,tkobject):
        tkobject.title("Register page")
        width=900
        height=500
        screenwidth = tkobject.winfo_screenwidth()
        screenheight = tkobject.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        tkobject.geometry(alignstr)
        tkobject.resizable(width=False, height=False)

        

    def createlogin(self):
        pass


tkobject=tk.Tk()
loginpage=Login(tkobject)

tkobject.mainloop()