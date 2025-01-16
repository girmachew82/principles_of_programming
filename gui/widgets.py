import tkinter as tk



root  = tk.Tk()

root.title("Widgets")
root.geometry("400x400")

label = tk.Label(root, text="This is a label")
button = tk.Button(root, text="Click Me")
entry  = tk.Entry(root)
text = tk.Text(root,height=5, width=5)
python = tk.Checkbutton(root,text="Python")
java = tk.Checkbutton(root,text="Java")
php = tk.Checkbutton(root,text="PHP")


male  = tk.Radiobutton(root, text="Male", value="Male")
female  = tk.Radiobutton(root, text="Female", value="Female")

spin = tk.Spinbox(root, from_= 0,to =10)
list  = tk.Listbox(root)
scrol = tk.Scrollbar(root)

label.pack()
button.pack()
entry.pack()
text.pack()
python.pack()
java.pack()
php.pack()
male.pack()
female.pack()
spin.pack()
list.pack()
scrol.pack()

root.mainloop()