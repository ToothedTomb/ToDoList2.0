from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter as ttk
from tkinter import filedialog
import pickle
import easygui
#Added Self as it will fix the button and the return key to work together. :)
def copyTask():
    selected_task = lb.get(lb.curselection())
    root.clipboard_clear()
    root.clipboard_append(selected_task)
    root.update()
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

def newTask():
    task = my_entry.get("1.0", END)  # Retrieve all text from the Text widget
    task = task.strip()  # Remove leading and trailing whitespaces
    if task:
        lb.insert(END, task)
        my_entry.delete("1.0", END)  # Clear the Text widget
    else:
        root = tk.Tk()
        root.resizable(0, 0)
        root.title("Sorry I ran into an issue :(")

        labelTitle = ttk.Label(root, font=("Ubuntu", 26, "bold", "underline"), anchor='center', text="Sorry:")
        label = ttk.Label(root, font=("Ubuntu", 16, "bold",), anchor='center', text="There is nothing to add.")

        labelTitle.pack(side="top", fill="x", pady=1)
        label.pack(side="top", fill="x", pady=2)

        B1 = tk.Button(root, text="Exit", font=("ubuntu", 28), bg="grey", border=12,
                       activebackground='#2e80ea', command=root.destroy)
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
def our_command3():
    root = tk.Tk() 
    root.resizable(0,0)
    root.title("What is this software about?")

    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="What is this software about?")
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Simple open source ToDoList For Linux and FreeBSD.")

    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)

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

file_menu2= Menu(my_menu,background="grey",activebackground="#2e80ea",border="6")
file_menu= Menu(my_menu,background="grey",activebackground="#2e80ea",border="6")

my_menu.add_cascade(label="File:",font=("Ubuntu",18),activebackground="#2e80ea", menu=file_menu2)
my_menu.add_cascade(label="About:",font=("Ubuntu",18),activebackground="#2e80ea", menu=file_menu)
file_menu.add_command(label="Who made this software?",font=("Ubuntu",18),activebackground="#2e80ea",background="grey",command=our_command2) 
file_menu.add_command(label="What is this software about?",font=("Ubuntu",18),activebackground="#2e80ea",background="grey",command=our_command3) 
file_menu.add_command(label="Keyboard shortcuts:",font=("Ubuntu",18),activebackground="#2e80ea",background="grey",command=KeyboardShortcut) 

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='note.png'))
root.title('Objective Oasis!')
root.config(bg='pink')
root.resizable(width=False, height=False)

Label(root, text="Objective Oasis:", font=('Ubuntu 29 underline'),background="pink").pack(pady=16)
Label(root, text="You tasks list is here:", font=('Ubuntu 20 underline'),background="pink").pack(pady=16)


frame = Frame(root,bg='pink')
frame.pack(pady=10)
Label(root, text="Enter here some tasks:", font=('Ubuntu 20 underline'),background="pink").pack(pady=16)

lb = Listbox(
    frame,
    width=34,
    height=7,
    border=12,
    font=('Ubuntu', 22),
    bd=1,
    fg='black',
    selectbackground='#2e80ea',
    activestyle="none",

    
)
print(lb)



#This is code that is empty because people will update this code. :)
task_list = [
      "Task"
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame,orient="vertical",background="#2e80ea",activebackground="purple")
sb.pack(side=RIGHT, fill=Y)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
sb2 = Scrollbar(frame,orient="horizontal",background="#2e80ea",activebackground="purple")
sb2.pack(side = BOTTOM, fill = X)
lb.config(xscrollcommand=sb2.set)
sb2.config(command=lb.xview)
#Add the listbox
lb.pack(side=TOP, fill=Y)
frame = Frame(root)
frame.pack(pady=10)
my_entry = Text(
    frame,
    font=('Ubuntu', 24),
    width=60,
    height=1,  # Specify the number of lines for the Text widget
    wrap="word",  # Wrap text at word boundaries


)
scrollbar_text_x = ttk.Scrollbar(
    frame,
    orient='vertical',
    command=my_entry.yview,
    background="#2e80ea",
    activebackground="purple"
)

my_entry.config(xscrollcommand=scrollbar_text_x.set)#Add the entry box.
scrollbar_text_x.pack(side="right", fill=Y)
my_entry.pack(pady=11)
Label(root, text="Press one of these buttons to do an action:", font=('Ubuntu 20 underline'),background="pink").pack(pady=16)

button_frame = Frame(root)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='New Task',
    font=('Ubuntu 24'),
    bg='grey',
    activebackground="#2e80ea",
    padx=12,
    pady=12,
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
    padx=12,
    pady=12,
    border=10,
    command=deleteTask
)
copyTask_btn = Button(
    button_frame,
    bg='grey',  # Set the background color to pink
    text='Copy Task',
    font=('Ubuntu 24'),
    border=10,
    activebackground="#2e80ea",
    padx=12,
    pady=12,
    command=copyTask
)



delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)
copyTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

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
def save_list():
    file_name = easygui.filesavebox(default=".dat", filetypes=["*.dat"])
    if file_name:
        # Delete crossed-off items before saving
        count = 0
        while count < lb.size():
            if lb.itemcget(count, "fg") == "#dedede":
                lb.delete(lb.index(count))
            else:
                count += 1

        # grab all the stuff from the list
        stuff = lb.get(0, END)

        # Open the file
        output_file = open(file_name, 'wb')

        # Actually add the stuff to the file
        pickle.dump(stuff, output_file)
    messagebox.showinfo(
        "Saved without issues","You have saved the file without errors!!!"
    )

def open_list():
    file_name = filedialog.askopenfilename(title="Open File", filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))
    if file_name:
        # Delete currently open list
        lb.delete(0, END)

        # Open the file
        input_file = open(file_name, 'rb')

        # Load the data from the file
        stuff = pickle.load(input_file)

        # Output stuff to the screen
        for item in stuff:
            lb.insert(END, item)


file_menu2.add_command(label="Save",font=("Ubuntu",18),activebackground="#2e80ea",background="grey",command=save_list) 
file_menu2.add_command(label="Open",font=("Ubuntu",18),activebackground="#2e80ea",background="grey",command=open_list) 

root.protocol("WM_DELETE_WINDOW", on_closing)
tk.mainloop()