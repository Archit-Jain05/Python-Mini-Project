import tkinter as tk

class ScrollableFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # Create a canvas object and a vertical scrollbar for scrolling it
        self.scrollbar = tk.Scrollbar(self, orient="vertical")
        self.scrollable_frame = tk.Canvas(self, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.scrollable_frame.yview)
        self.scrollbar.pack(side="right", fill="y")

        # Add a frame to the canvas which will be scrolled with it
        self.scrollable_frame.bind("<Configure>", self.set_scroll_region)
        self.scrollable_frame_frame = tk.Frame(self.scrollable_frame)
        self.scrollable_frame.create_window((0, 0), window=self.scrollable_frame_frame, anchor="nw")

        # Pack the scrollable frame inside the main frame
        self.scrollable_frame.pack(side="left", fill="both", expand=True)

    def set_scroll_region(self, event):
        self.scrollable_frame.configure(scrollregion=self.scrollable_frame.bbox("all"))
