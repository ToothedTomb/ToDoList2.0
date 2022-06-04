from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter as ttk

#Added Self as it will fix the button and the return key to work together. :)
def EnterKeyPress(self):
    self.task = my_entry.get()
    if self.task !="":
        lb.insert(END, self.task)
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
def newTask():
    task = my_entry.get()
    if task !="":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        root = tk.Tk() 
        root.resizable(0,0)
        root.title("Sorry I ran into an issue :(")

        labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Sorry:")
        label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="There is nothing to add.")

        labelTitle.pack(side="top",fill="x",pady=1)
        label.pack(side="top", fill="x", pady=2)


        B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="grey",border=12,activebackground='#2e80ea', command = root.destroy)
        B1.pack()

    
def deleteTask():
        lb.delete(ANCHOR)

def pressDelKey(self):
    lb.delete(ANCHOR)
    
root = tk.Tk()
root.geometry('680x855')
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
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Simple open source ToDoList For Linux, FreeBSD and Windows.")

    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)


    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="grey",border=12,activebackground='#2e80ea', command = root.destroy)
    B1.pack()
def KeyboardShortcut():
    root = tk.Tk() 
    root.resizable(0,0)
    root.title("Keyboard shortcuts?")

    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Keyboard shortcuts:")
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Press enter key will add a task.")
    label2 = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Press delete key will delete a task.")


    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    label2.pack(side="top", fill="x", pady=3)


    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="grey",border=12,activebackground='#2e80ea', command = root.destroy)
    B1.pack()
file_menu= Menu(my_menu,background="grey",activebackground="#2e80ea",border="6")
my_menu.add_cascade(label="About:",font=("Ubuntu",18),background="grey",activebackground="#2e80ea", menu=file_menu)
file_menu.add_command(label="Who made this software?",font=("Ubuntu",18),activebackground="#2e80ea",background="grey",command=our_command2) 
file_menu.add_command(label="What is this software about?",font=("Ubuntu",18),activebackground="#2e80ea",background="grey",command=our_command3) 
file_menu.add_command(label="Keyboard shortcuts:",font=("Ubuntu",18),activebackground="#2e80ea",background="grey",command=KeyboardShortcut) 

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='note.png'))
root.title('ToDoList 8.0 For Linux!')
root.config(bg='pink')
root.resizable(width=False, height=False)

Label(root, text="ToDoList 8.0 For Linux!", font=('Ubuntu 29 underline'),background="pink").pack(pady=16)
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




task_list = [
    "Install Ubuntu",
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame,orient="vertical")
sb.pack(side=RIGHT, fill=Y)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
sb2 = Scrollbar(frame,orient="horizontal")
sb2.pack(side = BOTTOM, fill = X)
lb.config(xscrollcommand=sb2.set)
sb2.config(command=lb.xview)
#Add the listbox
lb.pack(side=TOP, fill=X)

my_entry = Entry(
    root,
    font=('Ubuntu', 24),
    width=34, highlightthickness=(4),

)
scrollbar = ttk.Scrollbar(
    my_entry,
    orient='horizontal',
    command=my_entry.xview
)




my_entry.pack(pady=20)

#Add the entry box.




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
#When the user press the return key then they will submit a new task
root.bind('<Return>', EnterKeyPress)
# pressDelKey will allow people to delete their tasks with the delete key.
root.bind('<Delete>', pressDelKey)
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
    root = tk.Toplevel()  
    root.resizable(0,0)
    root.title("Confirm to exit the software:")
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='note.png'))


    labelTitle = tk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Confirm to exit the software:")
    label = tk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Are you sure you want to leave this software?")
    label2 = tk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="If you leave all the data will be deleted.")

    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    label2.pack(side="top", fill="x", pady=3)

    B1 = tk.Button(root, text="Yes",font=("ubuntu",24),bg='grey',border="10", activebackground="#2e80ea", command = root.quit)

    B2 = tk.Button(root, text="No",font=("ubuntu",24),bg='grey',border="10", activebackground="#2e80ea", command = root.destroy)
    B1.pack(side=tk.LEFT, anchor=CENTER)
    B2.pack(side=tk.RIGHT, anchor=CENTER)
root.protocol("WM_DELETE_WINDOW", on_closing)
tk.mainloop()