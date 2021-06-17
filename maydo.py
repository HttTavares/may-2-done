import tkinter as tk

class MayDoWindow():
    def __init__(self):
        self.window = tk.Toplevel()
        self.Header = tk.Frame(self.window)
        self.lbl = tk.Label(self.Header, text = "seila")
        self.Header.pack()
        self.lbl.pack()
