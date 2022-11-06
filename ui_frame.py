import tkinter as tk

import about as about
import new_connect as new_connect
import open_connect as open_connect


class UIFrame(tk.Frame):
    def __init__(self, master, main_window_self, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)

        self.master = master

        self.entry_broker_text = tk.StringVar()
        self.entry_broker = tk.Entry(self, textvariable=self.entry_broker_text)
        self.entry_broker.pack()

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

        # menu
        menubar = tk.Menu(main_window_self)
        main_window_self.config(menu=menubar)

        menu_connect = tk.Menu(menubar, tearoff=0)
        menu_connect.add_command(label='New Connect',
                                 command=self.new_connect_window)
        menu_connect.add_command(label='Open Connect',
                                 command=self.open_connect_window)
        menu_connect.add_separator()
        menu_connect.add_command(label='Exit', command=main_window_self.quit)
        menubar.add_cascade(label="Connect", menu=menu_connect)

        menu_help = tk.Menu(menubar, tearoff=0)
        menu_help.add_command(label='Help')
        menu_help.add_command(label='About', command=self.about_window)
        menubar.add_cascade(label="Help", menu=menu_help)

        # status bar
        status_text = tk.StringVar()
        status_text.set("Ready")
        status = tk.Label(main_window_self, textvariable=status_text,
                          relief=tk.SUNKEN, anchor="w")
        status.pack(side=tk.BOTTOM, fill=tk.X)

    def about_window(self):
        about.AboutWindow(self.master)

    def new_connect_window(self):
        new_connect.NewConnect(self.master)

    def open_connect_window(self):
        open_connect.OpenConnect(self.master)
        # print("qq")
        # print(broker, port, username, password)
