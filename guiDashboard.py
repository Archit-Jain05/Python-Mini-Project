from tkinter import *
from PIL import Image, ImageTk
from datetime import *
import datetime 
from tkinter import messagebox
import tkinter as tk
from UserDatabase import userdata
from tkinter import font as tkFont

opt=[0,0,0,0,0,0,0]

class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title("VIA News Dashboard")
        self.window.geometry("1366x768")
        self.window.state("zoomed")
        self.window.config(background = '#A2C7E5')

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

        self.header = Frame(self.window , bg = 'white')
        self.header.place(x=300 , y=0 , width=2000, height=60)

        self.logout_text = Button(self.header , text="Logout" , bg="#32cf8e" , font=("" , 13 , "bold") , bd=0 , fg="white" , cursor='hand2' ,  activebackground='#32cf8e',command=logout)
        self.logout_text.place(x=1150 , y=15)


        #===================================================
        #=====================SIDEBAR=======================
        #===================================================

        self.sidebar = Frame(self.window , bg='white')
        self.sidebar.place(x=0 , y=0 , width=300 , height=800)
        #logo
        
        self.logoImage = Image.open('Images\\acc5.png')
        resize_image = self.logoImage.resize((120, 120))
        photo = ImageTk.PhotoImage(resize_image)
        self.logo = Label(self.sidebar , image=photo , bg='#ffffff')
        self.logo.image = photo
        self.logo.place(x=80 , y=60)

        def home_red(window):
            window.destroy()
            window = Tk()
            window.protocol("WM_DELETE_WINDOW", lambda:on_closing(window))
            sc1=Homepage(window)
            window.mainloop()

        self.logoImage = Image.open('Images\\home.png')
        resize_image = self.logoImage.resize((30,30))
        photo = ImageTk.PhotoImage(resize_image)
        self.logo = Button(self.sidebar , image=photo , bg='#ffffff',border=0,command=lambda:home_red(window))
        self.logo.image = photo
        self.logo.place(x=20 , y=9)
        #name
        self.brandname = Label(self.sidebar , text='My Account' , bg='#A2C7E5' , font=("",15,"bold"))
        self.brandname.place(x=80 , y=200)

        #===================================================
        #======================BODY=========================
        #===================================================
        
        self.heading = Label(self.window , text='Dashboard' , font=("",13,"bold"),fg='#0064d3',bg='#A2C7E5')
        self.heading.place(x=325 , y=70)

        #============Details pane===============
        self.bodyframe1 = Frame(self.window , bg='#ffffff')
        self.bodyframe1.place(x=328 , y=110, width=1150, height=350)
        self.user=Text(self.bodyframe1,width=25,height=1,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light' , 14,),background="#dfdfdf")
        self.user.place(x=55,y=80)
        file1=open("MyFiles/credentials.txt","r+")
        usn=file1.readline(-1)
        username=file1.readline(-1)
        file1.close()
        
        self.user.insert(END, usn)
        self.user.config(state="disabled")
        self.label=Label(self.bodyframe1,text="Username :",fg='black',bg='white',font=("Microsoft YaHei UI Light" , 16))
        self.label.place(x=50,y=40)
        
        
        self.passw=Entry(self.bodyframe1,width=25,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light' , 14))
        self.passw.place(x=55,y=160)
        file1=open("MyFiles/credentials.txt","r+")
        password=file1.readlines()
        file1.close()
        #print(password)
        self.passw.insert(0,password[1])
        self.label2=Label(self.bodyframe1,text="Password :",fg='black',bg='white',font=("Microsoft YaHei UI Light" , 16))
        self.label2.place(x=50,y=120)

        self.age=Entry(self.bodyframe1,width=25,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light' , 14,),background="white")
        self.age.insert(0, "18")
        self.age.place(x=500,y=80)
        self.label2=Label(self.bodyframe1,text="Age :",fg='black',bg='white',font=("Microsoft YaHei UI Light" , 16))
        self.label2.place(x=500,y=40)
        
        
        self.contr=Entry(self.bodyframe1,width=25,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light' , 14))
        self.contr.place(x=500,y=160)
        file1=open("MyFiles/credentials.txt","r+")
        password=file1.readlines()
        file1.close()
        #print(password)
        self.contr.insert(0,"India")
        self.label3=Label(self.bodyframe1,text="Country :",fg='black',bg='white',font=("Microsoft YaHei UI Light" , 16))
        self.label3.place(x=500,y=120)

        def update_command():
            userdata.updateuser(username,password,opt,age="18",country="India")

        ft = tkFont.Font(family='Microsoft YaHei UI Light',size=12)
        finish = Button(self.bodyframe1,width=15,text="Update User",border=0 , bg='white',cursor='hand2',fg='#57a1f8',font=ft,command=update_command)
        finish.place(x=1000,y=300)

        GCheckBox_851=tk.Checkbutton(window)
        ft = tkFont.Font(family='Microsoft YaHei UI Light',size=12)
        GCheckBox_851["font"] = ft
        GCheckBox_851["fg"] = "#333333"
        GCheckBox_851["bg"] = "#A2C7E5"
        GCheckBox_851["justify"] = "center"
        GCheckBox_851["text"] = "Politics"
        GCheckBox_851.place(x=50,y=250)
        GCheckBox_851["offvalue"] = "0"
        GCheckBox_851["onvalue"] = "1"
        GCheckBox_851["command"] = self.GCheckBox_851_command
        ft = tkFont.Font(family='Microsoft YaHei UI Light',size=12)


        GCheckBox_463=tk.Checkbutton(window)
        ft = tkFont.Font(family='Microsoft YaHei UI Light',size=12)
        GCheckBox_463["font"] = ft
        GCheckBox_463["fg"] = "#333333"
        GCheckBox_463["bg"] = "#A2C7E5"
        GCheckBox_463["justify"] = "center"
        GCheckBox_463["text"] = "Sports"
        GCheckBox_463.place(x=50,y=290)
        GCheckBox_463["offvalue"] = "0"
        GCheckBox_463["onvalue"] = "1"
        GCheckBox_463["command"] = self.GCheckBox_463_command

        GCheckBox_830=tk.Checkbutton(window)
        ft = tkFont.Font(family='Microsoft YaHei UI Light',size=12)
        GCheckBox_830["font"] = ft
        GCheckBox_830["fg"] = "#333333"
        GCheckBox_830["bg"] = "#A2C7E5"
        GCheckBox_830["justify"] = "center"
        GCheckBox_830["text"] = "Entertainment"
        GCheckBox_830.place(x=50,y=330)
        GCheckBox_830["offvalue"] = "0"
        GCheckBox_830["onvalue"] = "1"
        GCheckBox_830["command"] = self.GCheckBox_830_command

        GCheckBox_917=tk.Checkbutton(window)
        ft = tkFont.Font(family='Microsoft YaHei UI Light',size=12)
        GCheckBox_917["font"] = ft
        GCheckBox_917["fg"] = "#333333"
        GCheckBox_917["bg"] = "#A2C7E5"
        GCheckBox_917["justify"] = "center"
        GCheckBox_917["text"] = "Weather"
        GCheckBox_917.place(x=50,y=370)
        GCheckBox_917["offvalue"] = "0"
        GCheckBox_917["onvalue"] = "1"
        GCheckBox_917["command"] = self.GCheckBox_917_command

        GCheckBox_510=tk.Checkbutton(window)
        ft = tkFont.Font(family='Microsoft YaHei UI Light',size=12)
        GCheckBox_510["font"] = ft
        GCheckBox_510["fg"] = "#333333"
        GCheckBox_510["bg"] = "#A2C7E5"
        GCheckBox_510["justify"] = "center"
        GCheckBox_510["text"] = "Crime"
        GCheckBox_510.place(x=50,y=410)
        GCheckBox_510["offvalue"] = "0"
        GCheckBox_510["onvalue"] = "1"
        GCheckBox_510["command"] = self.GCheckBox_510_command

        GCheckBox_698=tk.Checkbutton(window)
        ft = tkFont.Font(family='Microsoft YaHei UI Light',size=12)
        GCheckBox_698["font"] = ft
        GCheckBox_698["fg"] = "#333333"
        GCheckBox_698["bg"] = "#A2C7E5"
        GCheckBox_698["justify"] = "center"
        GCheckBox_698["text"] = "Science and Technology"
        GCheckBox_698.place(x=50,y=450)
        GCheckBox_698["offvalue"] = "0"
        GCheckBox_698["onvalue"] = "1"
        GCheckBox_698["command"] = self.GCheckBox_698_command

        GCheckBox_598=tk.Checkbutton(window)
        ft = tkFont.Font(family='Microsoft YaHei UI Light',size=12)
        GCheckBox_598["font"] = ft
        GCheckBox_598["fg"] = "#333333"
        GCheckBox_598["bg"] = "#A2C7E5"
        GCheckBox_598["justify"] = "center"
        GCheckBox_598["text"] = "Wildlife"
        GCheckBox_598.place(x=50,y=490)
        GCheckBox_598["offvalue"] = "0"
        GCheckBox_598["onvalue"] = "1"
        GCheckBox_598["command"] = self.GCheckBox_598_command


       
    
    def GCheckBox_463_command(self):
        print("command")


    def GCheckBox_830_command(self):
        print("command")


    def GCheckBox_917_command(self):
        print("command")


    def GCheckBox_510_command(self):
        print("command")


    def GCheckBox_698_command(self):
        print("command")


    def GCheckBox_598_command(self):
        print("command")


    def GCheckBox_851_command(self):
        print("command")

class Homepage:
    def __init__(self, window):
        self.window = window
        self.window.title("VIA News Dashboard")
        self.window.geometry("1366x768")
        self.window.state("zoomed")
        self.window.config(background = '#dfdfdf')

        #window icon photo
        
        icon = PhotoImage(file='Images//img1.png')
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

        self.header = Frame(self.window , bg = '#A2C7E5')
        self.header.place(x=0 , y=0 , width=2000, height=60)
        self.accImage = Image.open('Images/img1.png')
        resize_image = self.accImage.resize((60,60))
        photo = ImageTk.PhotoImage(resize_image)
        self.logo = Button(self.header , image=photo , bg='#ffffff',border=0,command=lambda:dash(window))
        self.logo.image = photo
        self.logo.place(x=0 , y=0)
        self.accImage.close()

        ft = tkFont.Font(family='Microsoft YaHei UI Light',size=16)
        self.header1=Label(self.header,text="VIA News",font=ft,bg="#A2C7E5")
        self.header1.place(x=80,y=10)

        def dash(window):
            window.destroy()
            window = Tk()
            window.protocol("WM_DELETE_WINDOW", lambda:on_closing(window))
            sc1=Dashboard(window)
            window.mainloop()

        self.accImage = Image.open('Images\\acc5.png')
        resize_image = self.accImage.resize((40,40))
        photo = ImageTk.PhotoImage(resize_image)
        self.logo = Button(self.header , image=photo , bg='#ffffff',border=0,command=lambda:dash(window))
        self.logo.image = photo
        self.logo.place(x=1450 , y=7)

        #name
       
        #===================================================
        #======================BODY=========================
        #===================================================

        #============Details pane===============
        self.bodyframe1 = Frame(self.window , bg='#ffffff')
        self.bodyframe1.place(x=200 , y=110, width=1150, height=700)
        
def on_closing(window):
    if messagebox.askokcancel("Quit", "Are you sure you want to exit?"):
        window.destroy()

def win():
    window.protocol("WM_DELETE_WINDOW", lambda:on_closing(window))
    sc1=Homepage(window)
    window.mainloop()

window = Tk()
if __name__ == '__main__':
    win()

