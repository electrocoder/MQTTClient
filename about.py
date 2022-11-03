import tkinter as tk


class AboutWindow:
    def __init__(self, master):
        window = tk.Toplevel(master)
        window.grab_set()
        window.title("MQTT Client About")
        window.geometry("300x300")

        tk.Label(window, text="This is a new window").pack()
