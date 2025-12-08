# tkinter is a standard GUI (Graphical user interface) library in python.
# it lets you build windows,label,buttons,text boxs and more - just like apps with a user interface.

# build in with python (no need to install separately)
# Good for building simple desktop applications.
# cross-platform (works on windows,macOS,linux)

import tkinter as tk  #import the tkinter file.

"""
# create the windows

root = tk.Tk()
root.title("My First UI")
root.geometry("300x200") #set width and height

# add a label

label = tk.Label(root,text="Hello Tkinter!",font=("Arial",15))
label.pack(pady=20)

# add a button

def on_click():
    label.config(text="You clicked the button!")

button = tk.Button(root,text="Click me",command=on_click)
button.pack()

# start the GUI loop

root.mainloop()

"""

# create the simple calculator:-

root = tk.Tk()
root.title("Add two number calculator!")
root.geometry("400x300") # set width and height.

# label and entry boxes:-

tk.Label(root,text="Enter the number 1:").pack(pady=5)
num1_entry = tk.Entry(root)
num1_entry.pack()

tk.Label(root,text="Enter the number 2:").pack(pady=5)
num2_entry = tk.Entry(root)
num2_entry.pack()

# result label
result_label = tk.Label(root,text="Result will appear here!")
result_label.pack(pady=10)

# add two numbers

def add_numbers():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        total = num1 + num2
        result_label.config(text=f"Result : {total}")
    except ValueError:
        result_label.config(text="Please enter valid number")


# Button

tk.Button(root,text="Add",command=add_numbers).pack(pady=5)

# run the app

root.mainloop()

