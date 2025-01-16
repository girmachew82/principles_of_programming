import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


def login():
    usename = user_name.get()
    pasord = password.get()
    print(user_name.get())
    print(password.get())
    if not usename  or not pasord:
        messagebox.showerror("Error","Username and password are required")
    else:
        root.destroy()
        dash()

def clear():
    user_name.delete(0, tk.END)
    password.delete(0, tk.END)

def dash():
    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("400x400")
    menu = tk.Menu(dashboard)
    dashboard.config(menu=menu)
    filemenu = tk.Menu(menu)
    menu.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="New", command=NewFile)
    filemenu.add_command(label="Open...", command=OpenFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=dashboard.quit)

    helpmenu = tk.Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)
    dashboard.mainloop()

def NewFile():
    print("New File!")
def OpenFile():
    name = askopenfilename()
    print(name)
def About():
    print("This is a simple example of a menu")
   


root = tk.Tk()
root.title("Login")
root.geometry("300x200")

label = tk.Label(root, text="Username:").grid(row=0, column=0, pady=20, padx=20)
user_name = tk.Entry(root)
user_name.grid(row=0, column=1)

label = tk.Label(root, text="Password:").grid(row=1, column=0, pady=5, padx=20)
password = tk.Entry(root, show="*")
password.grid(row=1, column=1)

login_btn = tk.Button(root, text="Login", command=login).grid(row=2, column=0)
clear_btn = tk.Button(root, text="Clear", command=clear).grid(row=2, column=1)

root.mainloop()