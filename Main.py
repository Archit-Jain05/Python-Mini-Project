import tkinter as tk
from tkinter import *
from tkinter import messagebox
from UserDatabase import userdata
from tkinter import font as tkFont
import guiDashboard

f=open("MyFiles/credentials.txt","a")

class Login:
    def __init__(self,root,frame):
        root.title("Login to VIA News")
        l1=Label(root,image=img, bg='white').place(x=48,y=-2)
        frame = Frame(root, width=350,height=390,bg='white')
        frame.place(x=480,y=70)
        heading = Label(frame, text="LOGIN" , fg='#57a1f8' , bg='white' , font=("Microsoft YaHei UI Light" , 23 , 'bold'))
        heading.place(x=100,y=5)

        

        usn=""
        passw=""
        
        def on_enter(e):
            user.delete(0,'end')
        def on_leave(e):
            name=user.get()
            if name=="":
                user.insert(0,"Username")

        
        user=Entry(frame,width=36,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light' , 11))
        user.place(x=30,y=80)
        user.insert(0,"Username")
        user.bind('<FocusIn>' , on_enter)
        user.bind('<FocusOut>' , on_leave)

        f1=Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
        #-------------------------------------
        def on_enter(e):
            code.delete(0,'end')
            code["show"]="*"
        def on_leave(e):
            name=code.get()
            if name=="":
                code.insert(0,"Password")
                code["show"]=""    
            

        code=Entry(frame,width=36,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light' , 11))
        code.place(x=30,y=150)
        code.insert(0,"Password")
        code.bind('<FocusIn>' , on_enter)
        code.bind('<FocusOut>' , on_leave)

        
        check=tk.BooleanVar()
        GCheckBox_500=tk.Checkbutton(frame,variable=check)
        ft = tkFont.Font(family='Microsoft YaHei UI Light',size=12)
        GCheckBox_500["font"] = ft
        GCheckBox_500["fg"] = "#000000"
        GCheckBox_500["bg"] = "white"
        GCheckBox_500["justify"] = "center"
        GCheckBox_500["text"] = "Stay signed in"
        GCheckBox_500.place(x=80,y=300,width=172,height=40)
        GCheckBox_500["offvalue"] = "0"
        GCheckBox_500["onvalue"] = "1"
        GCheckBox_500["command"] = lambda:self.GCheckBox_500_command(check)
        
        f2=Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

        def hit_enter(self):
            Login.loginbtn_command(user,code,check)
        root.bind('<Return>', hit_enter)
        #-------------------------------------
        l1=Button(frame,width=39,pady=7,text="Sign in",bg='#57a1f8',fg='white',border=0,command=lambda:Login.loginbtn_command(user,code,check)).place(x=35,y=204)

        label=Label(frame,text="Don't Have an Account?",fg='black',bg='white',font=("Microsoft YaHei UI Light" , 9))
        label.place(x=75,y=270)

        sign_up = Button(frame,width=6,text="Sign up",border=0 , bg='white',cursor='hand2',fg='#57a1f8',command=self.regredirect_command)
        sign_up.place(x=215,y=270)
        

    def GCheckBox_500_command(self,check):
        ssi=check.get()
        print(ssi)

    def regredirect_command(self):
        print("Register")
        for widgets in frame.winfo_children():
            widgets.destroy()
        screen1=Preferences(root,frame)
    
    def loginbtn_command(user,code,check):
        ssi=check.get()
        usn=user.get()
        passw=code.get()
        if usn=="Username" and passw=="Password":
            f.truncate(0)
        else:
            if ssi==True:
                f.truncate(0)
                f.write("username:"+usn+"\npassword:"+passw)
        
        if userdata.validatelogin(usn,passw)==1:
            print("Succesful")
            root.destroy()
            guiDashboard.win()
        else:
            flag=messagebox.askretrycancel("Alert","Invalid Username/Password")
            if flag==False:
                root.destroy()

class Register:
    def __init__(self,root,frame):
        root.title("Register to VIA News")
        Label(root,image=img, border=0, bg='white').place(x=50,y=0)
        frame = Frame(root, width=350,height=390,bg='white')
        frame.place(x=480,y=70)
        heading = Label(frame, text="SIGN UP" , fg='#57a1f8' , bg='white' , font=("Microsoft YaHei UI Light" , 23 , 'bold'))
        heading.place(x=100,y=5)

        self.username=self.password=self.country=self.age=""
        self.pref=[]

        def on_enter(e):
            user.delete(0,'end')
        def on_leave(e):
            if user.get()=="":
                user.insert(0,"Username")

        user=Entry(frame,width=36,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light' , 11))
        user.place(x=30,y=80)
        user.insert(0,"Username")
        user.bind('<FocusIn>' , on_enter)
        user.bind('<FocusOut>' , on_leave)
        Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
        #------------------------------------
        def on_enter(e):
            code.delete(0,'end')
        def on_leave(e):
            if code.get()=="":
                code.insert(0,"Password")

        code=Entry(frame,width=36,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light' , 11))
        code.place(x=30,y=150)
        code.insert(0,"Password")
        code.bind('<FocusIn>' , on_enter)
        code.bind('<FocusOut>' , on_leave)
        Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
        #------------------------------------
        def on_enter(e):
            confirm_code.delete(0,'end')
        def on_leave(e):
            if confirm_code.get()=="":
                confirm_code.insert(0,"Confirm Password")

        confirm_code=Entry(frame,width=36,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light' , 11))
        confirm_code.place(x=30,y=220)
        confirm_code.insert(0,"Confirm Password")
        confirm_code.bind('<FocusIn>' , on_enter)
        confirm_code.bind('<FocusOut>' , on_leave)
        Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

        def hit_enter(self):
            print("Register hit")
        root.bind('<Return>', hit_enter)
        #------------------------------
        b2=Button(frame,width=39,pady=7,text="Next",bg='#57a1f8',fg='white',border=0,command=self.nextbtn_command).place(x=35,y=280)
        label1=Label(frame,text="I Have an Account!",fg='black',bg='white',font=("Microsoft YaHei UI Light" , 9))
        label1.place(x=90,y=340)

        signin = Button(frame,width=6,text="Sign In",border=0 , bg='white',cursor='hand2',fg='#57a1f8',command=self.loginredirect_command)
        signin.place(x=200,y=340)
        
    def nextbtn_command(self):
        pass

    def loginredirect_command(self):
        print("Login btn")
        for widgets in frame.winfo_children():
            widgets.destroy()
        screen1=Login(root,frame)

class Preferences(Register):
    def nextbtn_command(self):
        root.title("Set Your Preferences")
        l1=Label(root,image=img, bg='white').place(x=48,y=-2)
        frame = Frame(root, width=350,height=450,bg='white')
        frame.place(x=480,y=70)
        heading = Label(frame, text="Additional Information" , fg='#57a1f8' , bg='white' , font=("Microsoft YaHei UI Light" , 23 , 'bold'))
        heading.place(x=10,y=5)

        

        usn=""
        passw=""
        
        def on_enter(e):
            user.delete(0,'end')
        def on_leave(e):
            name=user.get()
            if name=="":
                user.insert(0,"Age")

        
        user=Entry(frame,width=36,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light' , 11))
        user.place(x=30,y=80)
        user.insert(0,"Age")
        user.bind('<FocusIn>' , on_enter)
        user.bind('<FocusOut>' , on_leave)

        f1=Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
        #-------------------------------------
        def on_enter(e):
            code.delete(0,'end')
            code["show"]="*"
            
        def on_leave(e):
            name=code.get()
            if name=="":
                code.insert(0,"Country")
                code["show"]=""    
            

        code=Entry(frame,width=36,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light' , 11))
        code.place(x=30,y=150)
        code.insert(0,"Country")
        code.bind('<FocusIn>' , on_enter)
        code.bind('<FocusOut>' , on_leave)

        
        
        
        f2=Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

        def hit_enter(self):
            Login.loginbtn_command(user,code)
        root.bind('<Return>', hit_enter)
        #-------------------------------------
        l1=Button(frame,width=20,pady=7,text="Next",bg='#57a1f8',fg='white',border=0,command=self.next_btn).place(x=200,y=300)

    def next_btn(self):
        print("show preference")



def on_closing():
    if messagebox.askokcancel("Quit", "Are you sure you want to exit?"):
        root.destroy()


f2=open("MyFiles/credentials.txt","r")
cont=f2.read()
print(cont)
if cont=="":
    root=tk.Tk()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.geometry('900x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)
    root.iconbitmap("Images/img1.ico")
    img = PhotoImage(file='Images/img1.png')
    frame = Frame(root,bg='white')
    frame.pack(fill="both")
    screen1=Login(root,frame)
    root.mainloop()
else:
    guiDashboard.win()
f.close()

