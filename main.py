import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox





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
        Loginredirect["command"] = self.Loginredirectbtn
	
    

    def Loginredirectbtn(self):
        rootlog.deiconify()
        rootreg.withdraw()
        
	

class Login:
    def __init__(self, rootlog):
        #setting title
        rootlog.title("Login Page VIA News")
        #setting window size
        width=900
        height=500
        screenwidth = rootlog.winfo_screenwidth()
        screenheight = rootlog.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        rootlog.geometry(alignstr)
        rootlog.resizable(width=False, height=False)


        GLabel_211=tk.Label(rootlog)
        ft = tkFont.Font(family='Times',size=43)
        GLabel_211["font"] = ft
        GLabel_211["fg"] = "#ff0202"
        GLabel_211["justify"] = "center"
        GLabel_211["text"] = "Login"
        GLabel_211.place(x=380,y=20,width=151,height=81)

        GLabel_825=tk.Label(rootlog)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_825["font"] = ft
        GLabel_825["fg"] = "#333333"
        GLabel_825["justify"] = "center"
        GLabel_825["text"] = "Username:"
        GLabel_825.place(x=340,y=150,width=116,height=32)

        GLineEdit_48=tk.Entry(rootlog)
        GLineEdit_48["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_48["font"] = ft
        GLineEdit_48["fg"] = "#333333"
        GLineEdit_48["justify"] = "left"
        GLineEdit_48["text"] = ""
        GLineEdit_48["relief"] = "flat"
        GLineEdit_48.place(x=360,y=180,width=207,height=30)

        GLabel_754=tk.Label(rootlog)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_754["font"] = ft
        GLabel_754["fg"] = "#333333"
        GLabel_754["justify"] = "center"
        GLabel_754["text"] = "Password:"
        GLabel_754.place(x=360,y=220,width=80,height=31)

        GLineEdit_573=tk.Entry(rootlog)
        GLineEdit_573["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_573["font"] = ft
        GLineEdit_573["fg"] = "#333333"
        GLineEdit_573["justify"] = "left"
        GLineEdit_573["text"] = ""
        GLineEdit_573["relief"] = "flat"
        GLineEdit_573.place(x=360,y=250,width=212,height=30)

        '''Regredirect=tk.Button(rootlog)
        Regredirect["bg"] = "#f0f0f0"
        Regredirect["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=10)
        Regredirect["font"] = ft
        Regredirect["fg"] = "#0038ff"
        Regredirect["justify"] = "center"
        Regredirect["text"] = "Dont have an Account? Sign up here."
        Regredirect["relief"] = "flat"
        Regredirect.place(x=330,y=350,width=250,height=30)
        Regredirect["command"] = self.Regredirectbtn'''

    

    def Regredirectbtn(self):
        rootlog.withdraw()
        rootreg.deiconify()


##############################--Frame Creation--##############################################
rootlog = tk.Tk()
loginpage = Login(rootlog)
rootreg = tk.Tk()
registerpage=Register(rootreg) 
rootreg.withdraw()

##############################--Closing window--#############################################
def on_closing():
    if messagebox.askyesno("Message Alert", "Do you want to quit?"):
        rootlog.destroy()
        rootreg.destroy()

rootlog.protocol("WM_DELETE_WINDOW", on_closing)
rootreg.protocol("WM_DELETE_WINDOW", on_closing)


rootlog.mainloop()
rootlog.mainloop()

