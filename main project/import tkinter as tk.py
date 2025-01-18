import tkinter as tk
from tkinter import messagebox

# Function for handling menu actions
def open_home():
    messagebox.showinfo("Home", "You clicked on Home!")

def open_about():
    messagebox.showinfo("About", "This is a simple navigation bar example.")

def open_exit():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Tkinter Navigation Bar Example")
root.geometry("400x300")

# Create a Menu bar
menu_bar = tk.Menu(root)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Home", command=open_home)
file_menu.add_command(label="Exit", command=open_exit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create the Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=open_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Add the menu bar to the root window
root.config(menu=menu_bar)

# Run the application
root.mainloop()
