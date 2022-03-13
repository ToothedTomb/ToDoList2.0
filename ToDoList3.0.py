from tkinter import *
from tkinter import messagebox
import tkinter as tk


def newTask():
    task = my_entry.get()
    if task !="":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Hey","Please enter some tasks you need to do.")
def deleteTask():
    lb.delete(ANCHOR)
    
root = tk.Tk()
root.geometry('540x460+500+230')
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='note.png'))
root.title('ToDoList 3.0!')
root.config(bg='purple')
root.resizable(width=False, height=False)

Label(root, text="Please enter some tasks you want to do:", font=('Ubuntu 10')).pack(pady=16)

frame = Frame(root)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Ubuntu', 13),
    bd=0,
    fg='purple',
    highlightthickness=0,
    selectbackground='pink',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [

    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    root,
    font=('Ubuntu', 18)
    )

my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('Ubuntu 14'),
    bg='pink',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Ubuntu 14'),
    bg='#add8e6',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

Label(root, text="Software was made by Jonathan Steadman.", font=('Ubuntu 10')).pack(pady=16)
tk.mainloop()