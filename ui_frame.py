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
            about.aboutWindow(master)

        menubar = tk.Menu(main_window_self)
        menu_connect = tk.Menu(menubar, tearoff=0)
        menu_connect.add_command(label="New Connect", command=donothing)
        menu_connect.add_command(label="Open Connect", command=donothing)
        menu_connect.add_separator()
        menu_connect.add_command(label="Exit", command=main_window_self.quit)
        menubar.add_cascade(label="Connect", menu=menu_connect)

        menu_help = tk.Menu(menubar, tearoff=0)
        menu_help.add_command(label="Help", command=donothing)
        menu_help.add_command(label="About", command=donothing)
        menubar.add_cascade(label="Help", menu=menu_help)

        main_window_self.config(menu=menubar)
