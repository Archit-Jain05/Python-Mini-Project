import tkinter as tk
from tkinter import *
from scrollframe import *

root = tk.Tk()
scrollable_frame = ScrollableFrame(root)
scrollable_frame.pack(fill="both", expand=True)
for i in range(50):
    tk.Frame(scrollable_frame.scrollable_frame_frame,pady=20,width=20,height=20).pack()
    
root.mainloop()
