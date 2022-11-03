import tkinter as tk


def about_window(master):
    # Toplevel object which will
    # be treated as a new window
    newWindow = tk.Toplevel(master)
    newWindow.grab_set()

    # sets the title of the
    # Toplevel widget
    newWindow.title("MQTT Client About")

    # sets the geometry of toplevel
    newWindow.geometry("300x300")

    # A Label widget to show in toplevel
    tk.Label(newWindow,
             text="This is a new window").pack()
