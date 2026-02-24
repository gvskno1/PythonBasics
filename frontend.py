import tkinter as tk

# create the main application window

root = tk.Tk()

root.title("Simple Tinker App")

root.geometry("200x100")

def say_hello():
    print("Hello, World!")

hello_button = tk.Button(root, text = 'Hello Me', command = say_hello)

hello_button.pack(pady=20)

root.mainloop()