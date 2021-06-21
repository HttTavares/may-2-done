import tkinter as tk
from db import project_data_base
from project_structure_interpreter import ProjectInterpreter




class MayDoWindow():
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title('MayDo')
        self.window.geometry('600x600')
        self.window.configure(bg = '#f2d74e')
        self.pdb = project_data_base
        self.proj_int = ProjectInterpreter(self.pdb)
        self.make_header()
        self.make_add_button()
        self.make_description()
        self.make_project_structure_writer()
        self.print_projects_button()



    def make_header(self):
        self.Header = tk.Frame(self.window)
        self.Header.place(x=0, y=0)
        self.name_label = tk.Label(self.Header,
            text = "Name: ")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.Header,
            text = 'name')
        self.name_entry.grid(row=0, column=1)
        self.duration_label = tk.Label(self.Header,
                text = "Duration: ")
        self.duration_label.grid(row=0, column=2)
        self.duration_entry = tk.Entry(self.Header,
            text = 'duration')
        self.duration_entry.grid(row=0, column=3)

    def make_description(self):
        self.project_description = tk.Text(self.window)
        self.project_description.place(x = 0,
            y = 30,
            height = 200,
            width = 600 )

    def make_project_structure_writer(self):
        self.project_structure_writer = tk.Text(self.window)
        self.project_structure_writer.place(x = 0,
            y = 250,
            height = 200,
            width = 600 )

    def add_to_db(self):
        # print(self.pdb)
        # print(project_data_base)
        self.pdb['maydo'].append({
            'name': self.name_entry.get(),
            'date': self.duration_entry.get(),
            'description': self.project_description.get("1.0", tk.END),
            'structure text': self.project_structure_writer.get("1.0", tk.END)
            })
        # print(self.pdb)
        # print(self.project_description)
        # print(type(self.project_description))
        # print(self.project_description.get())
        # print(self.pdb)
        # print(project_data_base)


    def make_add_button(self):
        self.add_button = tk.Button(self.window,
            text = "Add Project",
            command = self.add_to_db).place(x = 500, y = 500)

    def print_projects(self):
        print(project_data_base)

# test project_text
#asdassd
#asdadsad
##sadfdsarfa
###asdaddfsaaw


    def print_projects_button(self):
        self.print_proj_button = tk.Button( self.window,
        command = self.proj_int.project_interpreter_test,
        text = 'test interpreter' )
        self.print_proj_button.place(x = 30, y = 550)



# print(project_data_base)
