import tkinter
from tkinter import *

class Login(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("840x630")
        self.master.title("Welcome to the app")
        self.pack(fill=BOTH, expand=True)
        self.init_window()
        
    def init_window(self):
        Label(self,text="Log in to your account",bg='#57a1f8',fg='white',font=("Microsoft YaHei UI Light" , 23 , 'bold')).place(x=250,y=50)
        Label(self,text="Username",bg='white',fg='#57a1f8',font=('Microsoft YaHei UI Light' , 11)).place(x=200,y=150)
        Label(self,text="Password",bg='white',fg='#57a1f8',font=('Microsoft YaHei UI Light' , 11)).place(x=200,y=250)

        self.userEntry=Entry(self,width=36,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light' , 11))
        self.userEntry.place(x=200,y=180)
        self.userEntry.focus_set()
        
        self.passEntry=Entry(self,width=36,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light' , 11))
        self.passEntry.place(x=200,y=280)
        self.passEntry["show"]="*"
        
        def on_enter(e):
            self.userEntry.delete(0,'end')
        def on_leave(e):
            name=self.userEntry.get()
            if name=="":
                self.userEntry.insert(0,"Username")

        self.userEntry.bind('<FocusIn>' , on_enter)
        self.userEntry.bind('<FocusOut>' , on_leave)

        def on_enter(e):
            self.passEntry.delete(0,'end')
            self.passEntry["show"]="*"
        def on_leave(e):
            name=self.passEntry.get()
            if name=="":
                self.passEntry.insert(0,"Password")
                self.passEntry["show"]=""

        self.passEntry.bind('<FocusIn>' , on_enter)
        self.passEntry.bind('<FocusOut>' , on_leave)
        
        self.logbtn=Button(self,width=20,pady=7,text="Login",bg='#57a1f8',fg='white',border=0,command=self.loginbtn_command)
        self.logbtn.place(x=280,y=380)
        
    def loginbtn_command(self):
        a=self.userEntry.get()
        b=self.passEntry.get()
        print(a)
        print(b)
        if a=="" and b=="":
            print("You didn't type anything")
        elif a=="John" and b=="Doe":
            print("Successful login")
            self.nextbtn_command()
        else:
            print("Invalid username or password")
        
    def nextbtn_command(self):
        a=super().getdata()
        print(a)
        root.title("Set Your Preferences")
        l1=Label(root,image=img, bg='white').place(x=48,y=-2)
        frame = Frame(root, width=350,height=450,)
def nextbtn_command(self):
    a=super().getdata()
    print(a)
    root.title("Set Your Preferences")
    l1=Label(root,image=img, bg='white').place(x=48,y=-2)
    frame = Frame(root, width=350,height=450,bg='white')
    frame.pack(side='right',fill='y')
    lab1=Label(frame,text="Hello! "+a[0],fg='#57a1f8',font=('Microsoft YaHei UI Light' , 14)).place(x=10,y=30)
    lab2=Label(frame,text="Please tell us more about yourself",fg='black',font=('Microsoft YaHei UI Light' , 14)).place(x=10,y=60)
    lab3=Label(frame,text="Age",fg='#57a1f8',font=('Microsoft YaHei UI Light' , 11)).place(x=10,y=120)
    lab4=Label(frame,text="Gender",fg='#57a1f8',font=('Microsoft YaHei UI Light' , 11)).place(x=10,y=170)
    lab5=Label(frame,text="Country",fg='#57a1f8',font=('Microsoft YaHei UI Light' , 11)).place(x=10,y=220)
    lab6=Label(frame,text="City",fg='#57a1f8',font=('Microsoft YaHei UI Light' , 11)).place(x=10,y=270)
    e1=Entry(frame,width=10,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light' , 11))
    e1.place(x=100,y=120)
    e2=Entry(frame,width=10,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light' , 11))
    e2.place(x=100,y=170)
    e3=Entry(frame,width=10,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light' , 11))
    e3.place(x=100,y=220)
    e4=Entry(frame,width=10,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light' , 11))
    e4.place(x=100,y=270)
    btn=Button(frame,width=20,pady=7,text="Submit",bg='#57a1f8',fg='white',border=0,command=lambda:self.submit_command(e1.get(),e2.get(),e3.get(),e4.get()))
    btn.place(x=10,y=350)

    
