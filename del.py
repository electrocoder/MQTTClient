#!/usr/bin/python3
import tkinter as tk


class PygubuApp:
    def __init__(self, master=None):
        # build ui
        frame1 = tk.Frame(master)
        frame1.configure(height=200, width=200)
        label3 = tk.Label(frame1)
        label3.configure(text='Broker')
        label3.grid(column=0, row=0)
        entry3 = tk.Entry(frame1)
        entry3.grid(column=1, row=0)
        button1 = tk.Button(frame1)
        button1.configure(text='Connect')
        button1.grid(column=2, row=0)
        button2 = tk.Button(frame1)
        button2.configure(text='Disconnect')
        button2.grid(column=3, row=0)
        label4 = tk.Label(frame1)
        label4.configure(text='Publish')
        label4.grid(column=0, row=1)
        entry4 = tk.Entry(frame1)
        entry4.grid(column=1, row=1)
        button3 = tk.Button(frame1)
        button3.configure(text='Publish')
        button3.grid(column=2, row=1)
        listbox1 = tk.Listbox(frame1)
        listbox1.grid(column=1, row=2)
        label5 = tk.Label(frame1)
        label5.configure(text='Subscribe')
        label5.grid(column=0, row=3)
        listbox2 = tk.Listbox(frame1)
        listbox2.grid(column=1, row=3)
        button4 = tk.Button(frame1)
        button4.configure(text='button4')
        button4.grid(column=2, row=3)
        frame1.grid(column=0, row=0)

        # Main widget
        self.mainwindow = frame1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = PygubuApp(root)
    app.run()
