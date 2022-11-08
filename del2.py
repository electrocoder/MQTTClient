#!/usr/bin/python3
import tkinter as tk


class GridApp:
    def __init__(self, master=None):
        # build ui
        frame1 = tk.Frame(master)
        frame1.configure(height=300, width=300)

        # tk.Grid.rowconfigure(root, 0, weight=1)
        frame1.rowconfigure(3, weight=1)
        # tk.Grid.rowconfigure(root, 2, weight=1)
        # tk.Grid.rowconfigure(root, 3, weight=1)
        # tk.Grid.columnconfigure(root, 0, weight=1)
        # tk.Grid.columnconfigure(root, 1, weight=1)
        # tk.Grid.columnconfigure(root, 2, weight=1)
        # tk.Grid.columnconfigure(root, 3, weight=1)
        frame1.columnconfigure(1, weight=1)

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
        button3.configure(text='Publish E')
        button3.grid(column=4, row=1)

        label5 = tk.Label(frame1)
        label5.configure(text='Subscribe')
        label5.grid(column=0, row=2)

        button4 = tk.Button(frame1)
        button4.configure(text='button4')
        button4.grid(column=2, row=2)

        entry1 = tk.Entry(frame1)
        entry1.grid(column=3, row=1)

        entry2 = tk.Entry(frame1)
        entry2.grid(column=1, row=2)

        # scrollbar1 = tk.Scrollbar(frame1)
        # scrollbar1.configure(orient="vertical")
        # scrollbar1.grid(column=2, row=3, sticky="w")
        # scrollbar1.bind("<MouseWheel>", self.callback, add="")

        label1 = tk.Label(frame1)
        label1.configure(text='label1')
        label1.grid(column=2, row=1)

        listbox1 = tk.Listbox(frame1)
        listbox1.configure(activestyle="dotbox")
        listbox1.grid(column=1, row=3, sticky="NSEW")

        frame1.grid(column=0, row=0)

        # Main widget
        self.mainwindow = frame1

    def run(self):
        self.mainwindow.mainloop()

    def callback(self, event=None):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = GridApp(root)

    app.run()
