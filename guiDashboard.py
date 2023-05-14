from tkinter import *
from PIL import Image, ImageTk
from datetime import *
import datetime 
from tkinter import messagebox
import tkinter as tk

class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title("VIA News Dashboard")
        self.window.geometry("1366x768")
        self.window.state("zoomed")
        self.window.config(background = '#5c6169')

        #window icon photo
        
        icon = PhotoImage(file='Images\\img1.png')
        self.window.iconphoto(True, icon)
        #===================================================
        #=====================HEADER========================
        #===================================================
        def logout():
            file1=open("MyFiles/credentials.txt","r+")
            file1.truncate(0)
            file1.close()
            window.destroy()
            import Main
            exit()
        self.header = Frame(self.window , bg = '#009df4')
        self.header.place(x=300 , y=0 , width=2000, height=60)

        self.logout_text = Button(self.header , text="Logout" , bg="#32cf8e" , font=("" , 13 , "bold") , bd=0 , fg="white" , cursor='hand2' ,  activebackground='#32cf8e',command=logout)
        self.logout_text.place(x=1150 , y=15)
        #===================================================
        #=====================SIDEBAR=======================
        #===================================================
        self.sidebar = Frame(self.window , bg='#ffffff')
        self.sidebar.place(x=0 , y=0 , width=300 , height=800)

        #logo
        
        self.logoImage = Image.open('Images\\acc5.png')
        resize_image = self.logoImage.resize((120, 120))
        photo = ImageTk.PhotoImage(resize_image)
        self.logo = Label(self.sidebar , image=photo , bg='#ffffff')
        self.logo.image = photo
        self.logo.place(x=80 , y=60)

        #name
        self.brandname = Label(self.sidebar , text='My Account' , bg='#ffffff' , font=("",15,"bold"))
        self.brandname.place(x=80 , y=200)

        #===================================================
        #======================BODY=========================
        #===================================================
        self.heading = Label(self.window , text='Dashboard' , font=("",13,"bold"),fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=325 , y=70)

        #============BOFY FRAME 1===============
        self.bodyframe1 = Frame(self.window , bg='#ffffff')
        self.bodyframe1.place(x=328 , y=110, width=1040, height=350)
        #============BOFY FRAME 2===============
        self.bodyframe2 = Frame(self.window , bg='#009aa5')
        self.bodyframe2.place(x=328 , y=495, width=310, height=220)
        #============BOFY FRAME 3===============
        self.bodyframe3 = Frame(self.window , bg='#e21f26')
        self.bodyframe3.place(x=680 , y=495, width=310, height=220)
        #============BOFY FRAME 4===============
        self.bodyframe4 = Frame(self.window , bg='#ffcb1f')
        self.bodyframe4.place(x=1030 , y=495, width=310, height=220)


def on_closing(window):
    if messagebox.askokcancel("Quit", "Are you sure you want to exit?"):
        window.destroy()

def win():
    window = Tk()
    window.protocol("WM_DELETE_WINDOW", lambda:on_closing(window))
    Dashboard(window)
    window.mainloop()

if __name__ == '__main__':
    win()
