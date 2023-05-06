import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox


def launchLogin():
    print("Login func")
    if __name__ == "__main__":
        rootlog = tk.Tk()
        #app = Login(rootlog)
        rootlog.mainloop()





class Register:
    def __init__(self, rootreg):
        #setting title
        rootreg.title("Register to VIA News")
        #setting window size
        width=900
        height=500
        screenwidth = rootreg.winfo_screenwidth()
        screenheight = rootreg.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        rootreg.geometry(alignstr)
        rootreg.resizable(width=False, height=False)
        
        GLabel_211=tk.Label(rootreg)
        ft = tkFont.Font(family='Times',size=43)
        GLabel_211["font"] = ft
        GLabel_211["fg"] = "#ff0202"
        GLabel_211["justify"] = "center"
        GLabel_211["text"] = "Register"
        GLabel_211.place(x=355,y=20,width=200,height=81)

        GLabel_825=tk.Label(rootreg)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_825["font"] = ft
        GLabel_825["fg"] = "#333333"
        GLabel_825["justify"] = "center"
        GLabel_825["text"] = "Username:"
        GLabel_825.place(x=340,y=150,width=116,height=32)

        GLineEdit_48=tk.Entry(rootreg)
        GLineEdit_48["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_48["font"] = ft
        GLineEdit_48["fg"] = "#333333"
        GLineEdit_48["justify"] = "left"
        GLineEdit_48["text"] = ""
        GLineEdit_48["relief"] = "flat"
        GLineEdit_48.place(x=360,y=180,width=207,height=30)

        GLabel_754=tk.Label(rootreg)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_754["font"] = ft
        GLabel_754["fg"] = "#333333"
        GLabel_754["justify"] = "center"
        GLabel_754["text"] = "Password:"
        GLabel_754.place(x=360,y=220,width=80,height=31)

        GLineEdit_573=tk.Entry(rootreg)
        GLineEdit_573["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_573["font"] = ft
        GLineEdit_573["fg"] = "#333333"
        GLineEdit_573["justify"] = "left"
        GLineEdit_573["text"] = ""
        GLineEdit_573["relief"] = "flat"
        GLineEdit_573.place(x=360,y=250,width=212,height=30)

        Loginredirect=tk.Button(rootreg)
        Loginredirect["bg"] = "#f0f0f0"
        Loginredirect["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=10)
        Loginredirect["font"] = ft
        Loginredirect["fg"] = "#0038ff"
        Loginredirect["justify"] = "center"
        Loginredirect["text"] = "Have an Account? Sign in here."
        Loginredirect["relief"] = "flat"
        Loginredirect.place(x=330,y=350,width=250,height=30)
        Loginredirect["command"] = self.Loginredirect_command
	
    

    def Loginredirect_command(self):
        rootlog.deiconify()
        rootreg.withdraw()
        #launchLogin()
        
rootlog = tk.Tk()


rootreg = tk.Tk()

