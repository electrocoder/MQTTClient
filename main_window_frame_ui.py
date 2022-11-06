import tkinter as tk


class MainWindowFrameUI(tk.Frame):
    def __init__(self, main_window_frame, main_window_self, *args, **kwargs):
        super().__init__(master=main_window_frame, *args, **kwargs)

        self.main_window_frame = main_window_frame
        self.main_window_self = main_window_self

        row = 0
        column = 0

        self.label_broker = tk.Label(self, text="Broker")
        self.label_broker.grid(row=row, column=column)
        column += 1
        self.entry_broker_text = tk.StringVar(self)
        self.entry_broker = tk.Entry(self, textvariable=self.entry_broker_text)
        self.entry_broker.grid(row=row, column=column)

        column += 1

        self.button_connect = tk.Button(self,
                                        text="Connect",
                                        command=main_window_self.button_connect)
        self.button_connect.grid(row=row, column=column)

        column += 1

        self.button_disconnect = tk.Button(self,
                                           text="Disconnect",
                                           command=main_window_self.button_disconnect)
        self.button_disconnect.grid(row=row, column=column)

        row += 1
        column = 0

        self.entry_msg_text = tk.StringVar()
        self.entry_msg = tk.Entry(self, textvariable=self.entry_msg_text)
        self.entry_msg.grid(row=row, column=column)

        # menu
        menubar = tk.Menu(main_window_self)
        main_window_self.config(menu=menubar)

        menu_connect = tk.Menu(menubar, tearoff=0)
        menu_connect.add_command(label='New Connect',
                                 command=self.main_window_self.new_connect_window)
        menu_connect.add_command(label='Open Connect',
                                 command=self.main_window_self.open_connect_window)
        menu_connect.add_separator()
        menu_connect.add_command(label='Exit', command=main_window_self.quit)
        menubar.add_cascade(label="Connect", menu=menu_connect)

        menu_help = tk.Menu(menubar, tearoff=0)
        menu_help.add_command(label='Help')
        menu_help.add_command(label='About', command=self.main_window_self.about_window)
        menubar.add_cascade(label="Help", menu=menu_help)

        # status bar
        status_text = tk.StringVar()
        status_text.set("Ready")
        status = tk.Label(main_window_self, textvariable=status_text,
                          relief=tk.SUNKEN, anchor="w")
        status.pack(side=tk.BOTTOM, fill=tk.X)
