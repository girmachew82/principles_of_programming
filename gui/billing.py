reading ={
    "001":20,
    "002":22,
    "003":21,
    "004":23,
    "005":24,
    "006":25,
    "007":26,
    "008":27,
    "009":29,
    "010":28,    
}
def pay():
    id = customer_id.get()
    get  = reading.get(id)
    if get:
        print(get)
        messagebox.showinfo("Search", "Bill for "+id+"="+str(get))
    else:
        messagebox.showerror("Error ", "Not found")

import tkinter as tk
from tkinter import messagebox
root  = tk.Tk()
root.title("Bill")
root.geometry("400x300")

label = tk.Label(root, text="Customer ID").grid(row=0, column=0)
customer_id  = tk.Entry(root)
customer_id.grid(row=0, column=1)

pay  = tk.Button(root, text="Search", command=pay).grid(row=1, columnspan=2)

root.mainloop()