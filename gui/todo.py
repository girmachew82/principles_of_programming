import tkinter as tk
from tkinter import messagebox

# Predefined credentials
USERNAME = "admin"
PASSWORD = "password123"

# Function to validate login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome!")
        root.destroy()  # Close the login window
        open_todo_dashboard()  # Open the To-Do dashboard
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to open the To-Do dashboard
def open_todo_dashboard():
    dashboard = tk.Tk()
    dashboard.title("To-Do Dashboard")
    dashboard.geometry("400x400")

    # Task list
    tasks = []

    # Function to add a task
    def add_task():
        task = task_entry.get()
        if task:
            tasks.append(task)
            update_task_list()
            task_entry.delete(0, tk.END)

    # Function to remove a selected task
    def remove_task():
        selected_task = task_listbox.curselection()
        if selected_task:
            tasks.pop(selected_task[0])
            update_task_list()

    # Function to update the task list display
    def update_task_list():
        task_listbox.delete(0, tk.END)
        for task in tasks:
            task_listbox.insert(tk.END, task)

    # UI for To-Do List
    tk.Label(dashboard, text="To-Do List", font=("Arial", 16)).pack(pady=10)

    # Task entry and buttons
    task_entry = tk.Entry(dashboard, font=("Arial", 12))
    task_entry.pack(pady=10)
    tk.Button(dashboard, text="Add Task", command=add_task, bg="lightblue").pack(pady=5)
    tk.Button(dashboard, text="Remove Selected Task", command=remove_task, bg="lightcoral").pack(pady=5)

    # Task listbox
    task_listbox = tk.Listbox(dashboard, font=("Arial", 12), width=40, height=10)
    task_listbox.pack(pady=10)

    tk.Button(dashboard, text="Exit", command=dashboard.destroy, bg="lightgrey").pack(pady=10)

    dashboard.mainloop()

# Create the main window
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Username label and entry
tk.Label(root, text="Username:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password label and entry
tk.Label(root, text="Password:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, font=("Arial", 12), show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login button
login_button = tk.Button(root, text="Login", font=("Arial", 12), command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=20)

# Run the main loop
root.mainloop()
