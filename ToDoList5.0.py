from tkinter import *
from tkinter import messagebox
import tkinter as tk


def newTask():
    task = my_entry.get()
    if task !="":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Sorry","There is nothing to add!")
def deleteTask():
    lb.delete(ANCHOR)
    
    
root = tk.Tk()
root.geometry('560x850')
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='note.png'))
root.title('ToDoList 5.0 For Linux!')
root.config(bg='pink')
root.resizable(width=False, height=False)

Label(root, text="ToDoList 5.0 For Linux!", font=('Ubuntu 29 underline'),background="pink").pack(pady=16)
Label(root, text="You tasks list is here:", font=('Ubuntu 19'),background="pink").pack(pady=16)


frame = Frame(root)
frame.pack(pady=10)
Label(root, text="Enter here some tasks:", font=('Ubuntu 19'),background="pink").pack(pady=16)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Ubuntu', 24),
    bd=0,
    fg='black',
    highlightthickness=0,
    selectbackground='#2e80ea',
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
    font=('Ubuntu', 24)
    )

my_entry.pack(pady=20)
Label(root, text="Press one of these buttons to do an action:", font=('Ubuntu 19'),background="pink").pack(pady=16)

button_frame = Frame(root)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add New Task',
    font=('Ubuntu 24'),
    bg='grey',
    activebackground="#2e80ea",
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Ubuntu 24'),
    bg='green',
    activebackground="#2e80ea",
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

Label(root, text="Software was made by Jonathan Steadman.", font=('Ubuntu 19'),background="pink").pack(pady=16)
tk.mainloop()