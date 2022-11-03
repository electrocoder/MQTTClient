import tkinter as tk

import about as about


class UIFrame(tk.Frame):
    def __init__(self, master, main_window_self, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)

        self.button_connect = tk.Button(self,
                                        text="Connect",
                                        command=main_window_self.button_connect)
        self.button_connect.pack()

        self.button_disconnect = tk.Button(self,
                                           text="Dur",
                                           command=main_window_self.button_disconnect)
        self.button_disconnect.pack()

        self.entry_msg_text = tk.StringVar()
        self.entry_msg = tk.Entry(self, textvariable=self.entry_msg_text)
        self.entry_msg.pack()

        def donothing():
            x = 0
            about.openNewWindow(master)



        menubar = tk.Menu(main_window_self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=main_window_self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        main_window_self.config(menu=menubar)
