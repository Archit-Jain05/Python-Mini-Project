import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_849=tk.Button(root)
        GButton_849["bg"] = "#f0f0f0"
        GButton_849["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=10)
        GButton_849["font"] = ft
        GButton_849["fg"] = "#0029ff"
        GButton_849["justify"] = "center"
        GButton_849["text"] = "Dont have an account? Sign up here"
        GButton_849.place(x=220,y=210,width=275,height=30)
        GButton_849["command"] = self.GButton_849_command

    def GButton_849_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
