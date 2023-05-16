import tkinter as tk
from tkinter import *
from scrollframe import *

root = tk.Tk()
scrollable_frame = ScrollableFrame(root)
scrollable_frame.pack(fill="both", expand=True)

for i in range(50):
    tk.Label(scrollable_frame.scrollable_frame_frame, text=f"Label {i}").pack()
    
root.mainloop()
