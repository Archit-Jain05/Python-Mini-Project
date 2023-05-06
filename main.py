import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
from login import *
from register import *





print("First screen opened")
loginpage = Login(rootlog)
registerpage=Register(rootreg) 

rootreg.withdraw()


def on_closing():
    if messagebox.askyesno("Message Alert", "Do you want to quit?"):
        rootlog.destroy()
        rootreg.destroy()

rootlog.protocol("WM_DELETE_WINDOW", on_closing)
rootreg.protocol("WM_DELETE_WINDOW", on_closing)

rootlog.mainloop()
rootreg.mainloop()

