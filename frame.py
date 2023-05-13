import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a frame
frame = tk.Frame(root, bg="white", bd=2,width=900,height=400)
frame.pack(side=tk.TOP, fill=tk.X)

# Create a label widget
label = tk.Label(frame, text="Hello, world!", font=("Arial", 12))
label.pack(side=tk.LEFT, padx=5, pady=5)

# Create a button widget
button = tk.Button(frame, text="Click me!", command=lambda: print("Button clicked!"))
button.pack(side=tk.RIGHT, padx=5, pady=5)

# Run the main loop
root.mainloop()
