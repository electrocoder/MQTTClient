import tkinter as tk

def openNewWindow(master):
    # Toplevel object which will
    # be treated as a new window
    newWindow = tk.Toplevel(master)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    tk.Label(newWindow,
             text="This is a new window").pack()