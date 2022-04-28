from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter as ttk

def newTask():
    task = my_entry.get()
    if task !="":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        root = tk.Tk() 
        root.resizable(0,0)
        root.title("Error")

        labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Sorry")
        label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="There is nothing to add.")

        labelTitle.pack(side="top",fill="x",pady=1)
        label.pack(side="top", fill="x", pady=2)


        B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="grey",border=12,activebackground='#2e80ea', command = root.destroy)
        B1.pack()    
def deleteTask():
    lb.delete(ANCHOR)

    
root = tk.Tk()
root.geometry('660x845')
my_menu= Menu(root)
root.config(menu=my_menu)
def our_command2():
    root = tk.Tk() 
    root.resizable(0,0)
    root.title("Who made this software?")

    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Who made this software?")
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Jonathan Steadman has made this software.")
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="grey",border=12,activebackground='#2e80ea', command = root.destroy)
    B1.pack()
def our_command3():
    root = tk.Tk() 
    root.resizable(0,0)
    root.title("What is this software about?")

    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="What is this software about?")
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Simple open source ToDoList For Linux and FreeBSD.")

    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)


    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="grey",border=12,activebackground='#2e80ea', command = root.destroy)
    B1.pack()
file_menu= Menu(my_menu,background="grey",activebackground="#2e80ea",border="6")
my_menu.add_cascade(label="About:",font=("Ubuntu",18),background="grey",activebackground="#2e80ea", menu=file_menu)
file_menu.add_command(label="Who made this software?",font=("Ubuntu",18),activebackground="#2e80ea",background="grey",command=our_command2) 
file_menu.add_command(label="What is this software about?",font=("Ubuntu",18),activebackground="#2e80ea",background="grey",command=our_command3) 

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='note.png'))
root.title('ToDoList 6.0 For Linux!')
root.config(bg='pink')
root.resizable(width=False, height=False)

Label(root, text="ToDoList 6.0 For Linux!", font=('Ubuntu 29 underline'),background="pink").pack(pady=16)
Label(root, text="You tasks list is here:", font=('Ubuntu 20 underline'),background="pink").pack(pady=16)


frame = Frame(root)
frame.pack(pady=10)
Label(root, text="Enter here some tasks:", font=('Ubuntu 20 underline'),background="pink").pack(pady=16)

lb = Listbox(
    frame,
    width=34,
    height=9,
    border=12,
    font=('Ubuntu', 22),
    bd=1,
    fg='black',
    highlightthickness=(4),
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
    font=('Ubuntu', 24),
    width=34, highlightthickness=(4),

    )

my_entry.pack(pady=20)
Label(root, text="Press one of these buttons to do an action:", font=('Ubuntu 20 underline'),background="pink").pack(pady=16)

button_frame = Frame(root)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add New Task',
    font=('Ubuntu 24'),
    bg='grey',
    activebackground="#2e80ea",
    padx=25,
    pady=25,
    border=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Remove Task',
    font=('Ubuntu 24'),
    bg='grey',
    activebackground="#2e80ea",
    padx=25,
    pady=25,
    border=10,
    command=deleteTask
)

delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)
def on_closing():
    if messagebox.askokcancel("Confirm to exit the software:", "This will delete everything in the list. Are you sure you want to exit?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
tk.mainloop()