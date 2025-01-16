import tkinter as tk
import ttk 
root  = tk.Tk()

root.title("Widgets")
root.geometry("400x400")

label = tk.Label(root, text="This is a label")
button = tk.Button(root, text="Click Me")
entry  = tk.Entry(root)
text = tk.Text(root,height=5, width=5)
chk = tk.Checkbutton(root,text="Option")
rad  = tk.Radiobutton(root, text="Male", value="Male")
spin = tk.Spinbox(root, from_= 0,to =10)
list  = tk.Listbox(root)
scrol = tk.Scrollbar(root)
combo = ttk

label.pack()
button.pack()
entry.pack()
text.pack()
chk.pack()
rad.pack()
spin.pack()
list.pack()
scrol.pack()

root.mainloop()