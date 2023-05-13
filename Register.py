import tkinter as tk
import tkinter.font as tkFont

class Register:
    def __init__(self, regroot):
        #setting title
        regroot.title("undefined")
        #setting window size
        width=900
        height=500
        screenwidth = regroot.winfo_screenwidth()
        screenheight = regroot.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        regroot.geometry(alignstr)
        regroot.resizable(width=False, height=False)

        regtitle=tk.Label(regroot)
        regtitle["cursor"] = "watch"
        ft = tkFont.Font(family='Times',size=43)
        regtitle["font"] = ft
        regtitle["fg"] = "#ff0000"
        regtitle["justify"] = "center"
        regtitle["text"] = "Register"
        regtitle.place(x=340,y=70,width=182,height=67)

        entry1=tk.Entry(regroot)
        entry1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entry1["font"] = ft
        entry1["fg"] = "#333333"
        entry1["justify"] = "left"
        entry1["text"] = ""
        entry1.place(x=310,y=190,width=240,height=30)

        usernamelabel=tk.Label(regroot)
        ft = tkFont.Font(family='Times',size=14)
        usernamelabel["font"] = ft
        usernamelabel["fg"] = "#333333"
        usernamelabel["justify"] = "left"
        usernamelabel["text"] = "Username :"
        usernamelabel.place(x=310,y=160,width=93,height=30)

        passlabel=tk.Label(regroot)
        ft = tkFont.Font(family='Times',size=12)
        passlabel["font"] = ft
        passlabel["fg"] = "#333333"
        passlabel["justify"] = "left"
        passlabel["text"] = "Password :"
        passlabel.place(x=310,y=230,width=80,height=33)

        entry2=tk.Entry(regroot)
        entry2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entry2["font"] = ft
        entry2["fg"] = "#333333"
        entry2["justify"] = "left"
        entry2["text"] = ""
        entry2.place(x=310,y=260,width=240,height=30)

        nextbtn=tk.Button(regroot)
        nextbtn["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=10)
        nextbtn["font"] = ft
        nextbtn["fg"] = "#ffffff"
        nextbtn["justify"] = "center"
        nextbtn["text"] = "Next"
        nextbtn.place(x=400,y=380,width=70,height=25)
        nextbtn["command"] = self.nextbtn_command

        relabel=tk.Label(regroot)
        ft = tkFont.Font(family='Times',size=12)
        relabel["font"] = ft
        relabel["fg"] = "#333333"
        relabel["justify"] = "center"
        relabel["text"] = "Re-enter Password :"
        relabel.place(x=310,y=300,width=132,height=30)

        entry3=tk.Entry(regroot)
        entry3["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entry3["font"] = ft
        entry3["fg"] = "#333333"
        entry3["justify"] = "left"
        entry3["text"] = ""
        entry3.place(x=310,y=330,width=241,height=30)

        redirectbtn=tk.Button(regroot)
        redirectbtn["bg"] = "#f0f0f0"
        redirectbtn["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=10)
        redirectbtn["font"] = ft
        redirectbtn["fg"] = "#0029ff"
        redirectbtn["justify"] = "center"
        redirectbtn["text"] = "Dont have an account? Sign up here"
        redirectbtn.place(x=300,y=420,width=245,height=30)
        redirectbtn["command"] = self.redirectbtn_command

    def nextbtn_command(self):
        print("next btn")

    def redirectbtn_command(self):
        print("signup btton pressed")

regroot = tk.Tk()
app = Register(regroot)
regroot.mainloop()


