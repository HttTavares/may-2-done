###################################### INITIALIZATION

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from maydo import MayDoWindow
from todo import ToDoWindow
from done import DoneWindow
# from project_structure_interpreter import ProjectInterpreter




app = tk.Tk()
app.title('May2Done')
app.geometry('600x600')
app.configure(bg = '#c57ae6')


###################################### MAYDO WINDOW

def open_maydo():
    MayDo = MayDoWindow()

MayDo_button = tk.Button(app,
    text='MayDo',
    command = open_maydo)
MayDo_button.grid(row = 0, column = 0)

###################################### TODO WINDOW

def open_todo():
    ToDo = ToDoWindow()

ToDo_button = tk.Button(app,
    text='ToDo',
    command = open_todo)
ToDo_button.grid(row = 0, column = 1)

###################################### DONE WINDOW

def open_done():
        Done = DoneWindow()

Done_button = tk.Button(app,
    text='Done',
    command = open_done)
Done_button.grid(row = 0, column = 2)


# def open_may():
#     maydo_window = tk.Toplevel()
#     lvl = tk.Label(maydo_window,
#         text="Hello World").pack()

# maydo_frame = tk.Frame(maydo_window)

#
# my_label = tk.Label(app, text = 'hello world!')
# my_label2 = tk.Label(app, text = 'hello world2!')
# my_label.grid(row=0, column=0)
# my_label2.grid(row=1, column=0)
#
# def test_function():
#     pass
#
# entry = tk.Entry(app)
# entry.grid(row=5, column = 1)
#
# my_button = tk.Button(app,
# text="click me",
# command = lambda: print(entry.get()) ,
# bg = "#777777")
#
# # state=tk.DISABLED
# my_button.grid(row=2, column=0)
# def update_thing():
#     if "May" not in comboExample["values"]:
#         comboExample["values"] = comboExample["values"] + ("May",)
#
# comboExample = tk.ttk.Combobox(app,
#                             values=[
#                                     "January",
#                                     "February",
#                                     "March",
#                                     "April"],
#                                     postcommand = update_thing)
#
# comboExample.grid(column=0, row=3)
# comboExample.current(1)
# print(comboExample.get())


#remove these later
open_maydo()





app.mainloop()
