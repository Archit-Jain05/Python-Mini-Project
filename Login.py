import tkinter as tk
import tkinter.font as tkFont
from tkinter import *



class Login:
    def __init__(self,root,frame):
        #setting title
       
        root.title("Login to VIA News")
        #setting window size
        width=900
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)
        root.bg="white"
        root.iconbitmap("img1.ico")
        

        loginlabel=tk.Label(frame)
        ft = tkFont.Font(family='Times',size=43)
        loginlabel["font"] = ft
        loginlabel["fg"] = "#ff0000"
        loginlabel["justify"] = "center"
        loginlabel["text"] = "Login"
        loginlabel.pack(pady=35)

        usernamelabel=tk.Label(frame)
        ft = tkFont.Font(size=19)
        usernamelabel["font"] = ft
        usernamelabel["fg"] = "#333333"
        usernamelabel["justify"] = "left"
        usernamelabel["text"] = "Username :"
        usernamelabel.pack(pady=0)

        entry1=tk.Entry(frame)
        entry1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=18)
        entry1["font"] = ft
        entry1["fg"] = "#333333"
        entry1["justify"] = "left"
        entry1.pack(pady=0)

        passlabel=tk.Label(frame)
        ft = tkFont.Font(size=19)
        passlabel["font"] = ft
        passlabel["fg"] = "#333333"
        passlabel["justify"] = "left"
        passlabel["text"] = "Password :"
        passlabel.pack(pady=0)

        entry2=tk.Entry(frame,show='*')
        entry2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=18)
        entry2["font"] = ft
        entry2["fg"] = "#333333"
        entry2["justify"] = "left"
        entry2["text"] = ""
        entry2.pack(pady=0)

        loginbtn=tk.Button(frame,width=15,border=4)
        loginbtn["bg"] = "#2da67b"
        ft = tkFont.Font(size=10)
        loginbtn["font"] = ft
        loginbtn["fg"] = "#ffffff"
        loginbtn["justify"] = "center"
        loginbtn["text"] = "Login"
        loginbtn.pack(pady=15)
        loginbtn["command"] = self.loginbtn_command

        regredirect=tk.Button(frame)
        regredirect["bg"] = "#f0f0f0"
        regredirect["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=10)
        regredirect["font"] = ft
        regredirect["fg"] = "#0029ff"
        regredirect["justify"] = "center"
        regredirect["text"] = "Dont have an account? Sign up here"
        regredirect.pack(pady=10)
        regredirect["command"] = self.regredirect_command
        
    def regredirect_command(self):
        print("Register")
        for widgets in frame.winfo_children():
            widgets.destroy()
        
        screen1=Register(root,frame)
  
    def loginbtn_command(self):
        print("Login")




class Register:
    def __init__(self,root,frame):
        #setting title
        
        root.title("Register to VIA News")
        #setting window size
        width=900
        height=500
        screenwidth =root.winfo_screenwidth()
        screenheight =root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        regtitle=tk.Label(frame)
        ft = tkFont.Font(family='Times',size=43)
        regtitle["font"] = ft
        regtitle["fg"] = "#ff0000"
        regtitle["justify"] = "center"
        regtitle["text"] = "Register"
        regtitle.pack()

        usernamelabel1=tk.Label(frame)
        ft = tkFont.Font(family='Times',size=14)
        usernamelabel1["font"] = ft
        usernamelabel1["fg"] = "#333333"
        usernamelabel1["justify"] = "left"
        usernamelabel1["text"] = "Username :"
        usernamelabel1.pack()

        entry1=tk.Entry(frame)
        entry1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entry1["font"] = ft
        entry1["fg"] = "#333333"
        entry1["justify"] = "left"
        entry1.pack()

        passlabel=tk.Label(frame)
        ft = tkFont.Font(family='Times',size=12)
        passlabel["font"] = ft
        passlabel["fg"] = "#333333"
        passlabel["justify"] = "left"
        passlabel["text"] = "Password :"
        passlabel.pack()

        entry2=tk.Entry(frame)
        entry2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entry2["font"] = ft
        entry2["fg"] = "#333333"
        entry2["justify"] = "left"
        entry2.pack()

        relabel=tk.Label(frame)
        ft = tkFont.Font(family='Times',size=12)
        relabel["font"] = ft
        relabel["fg"] = "#333333"
        relabel["justify"] = "center"
        relabel["text"] = "Re-Enter Password :"
        relabel.pack()

        entry3=tk.Entry(frame)
        entry3["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entry3["font"] = ft
        entry3["fg"] = "#333333"
        entry3["justify"] = "left"
        entry3["text"] = ""
        entry3.pack()

        nextbtn=tk.Button(frame)
        nextbtn["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=10)
        nextbtn["font"] = ft
        nextbtn["fg"] = "#ffffff"
        nextbtn["justify"] = "center"
        nextbtn["text"] = "Next"
        nextbtn.pack()
        nextbtn["command"] = self.nextbtn_command


        loginredirect=tk.Button(frame)
        loginredirect["bg"] = "#f0f0f0"
        loginredirect["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=10)
        loginredirect["font"] = ft
        loginredirect["fg"] = "#0029ff"
        loginredirect["justify"] = "center"
        loginredirect["text"] = "Have an account? Sign in here"
        loginredirect["command"] = self.loginredirect_command
        loginredirect.pack()

    def nextbtn_command(self):
        print("next btn")

    def loginredirect_command(self):
        print("Login btn")
        print("Register")
        for widgets in frame.winfo_children():
            widgets.destroy()
        
        screen1=Login(root,frame)



root=tk.Tk()
frame = tk.Frame(root,width=900,height=400)
frame.pack(fill="both")
screen1=Login(root,frame)
root.mainloop()