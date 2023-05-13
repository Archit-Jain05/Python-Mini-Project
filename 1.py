import tkinter as tk

def create_frame():
    new_frame = tk.Frame(window, bg='white', width=200, height=200) # Create a new frame
    new_frame.pack() # Add the new frame to the window

window = tk.Tk() # Create the main window
button = tk.Button(window, text='Create Frame', command=create_frame) # Create a button
button.pack() # Add the button to the window

window.mainloop() # Start the event loop
