#Creating a text editor practice

import tkinter as tk
from tkinter import filedialog,messagebox

root = tk.Tk()
root.title("Note Here")
root.geometry("1000x600")

text = tk.Text(
    root,
    wrap = tk.WORD,
    font = ("Times New Roman", 12)
)

text.pack(expand=True,fill=tk.BOTH)

#Create New file

def new_file():
    text.delete(1.0, tk.END)

#Open an existing file

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension = ".txt",
        filetypes = [("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END, file.read())

#Save a file

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension = ".txt",
        filetypes = [("Text files", "*,txt")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0,tk.END))
        messagebox.showinfo("Info", "File saved successfully!")

#--Menu Bar--

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)

menu.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()