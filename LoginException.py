from tkinter import messagebox

class LoginException(Exception):
    def __init__(self):
        super().__init__()
        print("Failed")
        flag=messagebox.askretrycancel("Alert","Invalid Username/Password")

    
