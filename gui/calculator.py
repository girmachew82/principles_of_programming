import tkinter as tk

# Function to update the expression in the entry box
def press(key):
    expression = entry.get() + str(key)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry widget for the calculator display
entry = tk.Entry(root, font=("Arial", 20), bd=8, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, height=2, width=5, command=calculate, bg="lightgreen")
    elif text == "C":
        button = tk.Button(root, text=text, height=2, width=5, command=clear, bg="lightcoral")
    else:
        button = tk.Button(root, text=text, height=2, width=5, command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the main loop
root.mainloop()
