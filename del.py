#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class PlaceApp:
    def __init__(self, master=None):
        # build ui
        frame1 = ttk.Frame(master)
        frame1.configure(height=300, width=500)
        label1 = ttk.Label(frame1)
        label1.configure(text='label1')
        label1.place(anchor="nw", x=0, y=0)
        entry1 = ttk.Entry(frame1)
        entry1.place(anchor="nw", x=45, y=0)
        button1 = ttk.Button(frame1)
        button1.configure(text='button1')
        button1.place(anchor="nw", x=245, y=0)
        button2 = ttk.Button(frame1)
        button2.configure(text='button2')
        button2.place(anchor="nw", x=350, y=0)
        label2 = ttk.Label(frame1)
        label2.configure(text='label2')
        label2.place(anchor="nw", x=0, y=30)
        entry2 = ttk.Entry(frame1)
        entry2.place(anchor="nw", x=45, y=30)
        button3 = ttk.Button(frame1)
        button3.configure(text='button3')
        button3.place(anchor="nw", x=278, y=30)
        frame1.place(anchor="nw", x=0, y=0)

        # Main widget
        self.mainwindow = frame1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = PlaceApp(root)
    app.run()
