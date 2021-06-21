import tkinter as tk
from db import project_data_base

class DoneWindow():
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title('Done')
        self.window.geometry('600x600')
        self.window.configure(bg = '#5beb63')
        self.pdb = project_data_base
        # self.make_header()
        # self.make_add_button()
        # self.make_description()
