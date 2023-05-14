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

        GCheckBox_500=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_500["font"] = ft
        GCheckBox_500["fg"] = "#333333"
        GCheckBox_500["justify"] = "center"
        GCheckBox_500["text"] = "   Stay signed in"
        GCheckBox_500.place(x=180,y=210,width=172,height=40)
        GCheckBox_500["offvalue"] = "0"
        GCheckBox_500["onvalue"] = "1"
        GCheckBox_500["command"] = self.GCheckBox_500_command

    def GCheckBox_500_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
