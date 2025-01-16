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
        open_dashboard()  # Open the dashboard
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to open the dashboard
def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("300x200")
    tk.Label(dashboard, text="Welcome to the Dashboard!", font=("Arial", 16)).pack(pady=20)
    tk.Button(dashboard, text="Exit", command=dashboard.destroy).pack(pady=20)
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
