import tkinter as tk
import tkinter.font as tkFont
from tkinter import *

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=900
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        GLabel_211=tk.Label(root)
        ft = tkFont.Font(family='Times',size=43)
        GLabel_211["font"] = ft
        GLabel_211["fg"] = "#ff0202"
        GLabel_211["justify"] = "center"
        GLabel_211["text"] = "Login"
        GLabel_211.place(x=380,y=20,width=151,height=81)

        GLabel_825=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_825["font"] = ft
        GLabel_825["fg"] = "#333333"
        GLabel_825["justify"] = "center"
        GLabel_825["text"] = "Username:"
        GLabel_825.place(x=340,y=150,width=116,height=32)

        GLineEdit_48=tk.Entry(root)
        GLineEdit_48["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_48["font"] = ft
        GLineEdit_48["fg"] = "#333333"
        GLineEdit_48["justify"] = "left"
        GLineEdit_48["text"] = ""
        GLineEdit_48["relief"] = "flat"
        GLineEdit_48.place(x=360,y=180,width=207,height=30)

        GLabel_754=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_754["font"] = ft
        GLabel_754["fg"] = "#333333"
        GLabel_754["justify"] = "center"
        GLabel_754["text"] = "Password:"
        GLabel_754.place(x=360,y=220,width=80,height=31)

        GLineEdit_573=tk.Entry(root)
        GLineEdit_573["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_573["font"] = ft
        GLineEdit_573["fg"] = "#333333"
        GLineEdit_573["justify"] = "left"
        GLineEdit_573["text"] = ""
        GLineEdit_573["relief"] = "flat"
        GLineEdit_573.place(x=360,y=250,width=212,height=30)

        GButton_703=tk.Button(root)
        GButton_703["bg"] = "#f0f0f0"
        GButton_703["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=10)
        GButton_703["font"] = ft
        GButton_703["fg"] = "#0038ff"
        GButton_703["justify"] = "center"
        GButton_703["text"] = "Dont have an Account? Sign up here."
        GButton_703["relief"] = "flat"
        GButton_703.place(x=330,y=350,width=250,height=30)
        GButton_703["command"] = self.GButton_703_command

    def GButton_703_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
