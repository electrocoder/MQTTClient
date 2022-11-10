import tkinter as tk


class MainWindowFrameUI(tk.Frame):
    def __init__(self, main_window_frame, main_window_self, *args, **kwargs):
        super().__init__(master=main_window_frame, *args, **kwargs)

        self.main_window_frame = main_window_frame
        self.main_window_self = main_window_self

        row = 0
        column = 0

        self.label_broker = tk.Label(self, text="Broker")
        self.label_broker.grid(row=row, column=column, sticky=tk.W)
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
                                           state=tk.DISABLED,
                                           command=main_window_self.button_disconnect)
        self.button_disconnect.grid(row=row, column=column, sticky=tk.W)

        row += 1
        column = 0

        # publich topic
        self.label_publich_topic = tk.Label(self, text="Publish Topic")
        self.label_publich_topic.grid(row=row, column=column, sticky=tk.W)

        column += 1
        self.entry_publich_topic_text = tk.StringVar(self)
        self.entry_publich_topic = tk.Entry(self,
                                            textvariable=self.entry_publich_topic_text)
        self.entry_publich_topic.grid(row=row, column=column)

        column += 1
        self.label_publich_msg_topic = tk.Label(self, text="Publish Message")
        self.label_publich_msg_topic.grid(row=row, column=column)

        column += 1
        self.entry_publich_topic_msg_text = tk.StringVar(self)
        self.entry_publich_msg_topic = tk.Entry(self,
                                                textvariable=self.entry_publich_topic_msg_text)
        self.entry_publich_msg_topic.grid(row=row, column=column)

        column += 1
        self.button_publich_topic = tk.Button(self,
                                              text="Publish",
                                              command=main_window_self.button_publish_topic)
        self.button_publich_topic.grid(row=row, column=column)

        row += 1
        column = 0

        # subscribe topic
        self.label_subscribe_topic = tk.Label(self, text="Subscribe Topic")
        self.label_subscribe_topic.grid(row=row, column=column, sticky=tk.W)
        self.label_subscribe_topic.grid(row=row, column=column, sticky=tk.W)

        column += 1
        self.entry_subscribe_topic_text = tk.StringVar(self)
        self.entry_subscribe_topic = tk.Entry(self,
                                              textvariable=self.entry_subscribe_topic_text)
        self.entry_subscribe_topic.grid(row=row, column=column)

        column += 1
        self.button_subscribe_topic = tk.Button(self,
                                                text="Subscribe",
                                                state=tk.DISABLED,
                                                command=main_window_self.button_subscribe_topic)
        self.button_subscribe_topic.grid(row=row, column=column)

        column += 1
        self.button_search = tk.Button(self,
                                                text="Search",
                                                state=tk.DISABLED,
                                                command=main_window_self.search)
        self.button_search.grid(row=row, column=column)

        row += 1
        column = 0

        # subscribe list
        self.listbox_message_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.listbox_message = tk.Listbox(self)
        self.listbox_message.config(
            yscrollcommand=self.listbox_message_scrollbar.set)
        self.listbox_message.grid(
            column=column,
            columnspan=column + 4,
            ipadx=220,
            row=row,
            rowspan=row + 4,
            sticky="w")
        self.listbox_message_scrollbar.config(
            command=self.listbox_message.yview)
        self.listbox_message_scrollbar.grid(row=row, column=column + 4,
                                            ipady=70)

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
        menu_help.add_command(label='Help', command=self.main_window_self.help)
        menu_help.add_command(label='About',
                              command=self.main_window_self.about_window)
        menubar.add_cascade(label="Help", menu=menu_help)

        # status bar
        self.connect_status_text = tk.StringVar()
        self.connect_status_text.set("...")
        self.connect_status = tk.Label(main_window_self,
                                       textvariable=self.connect_status_text,
                                       relief=tk.SUNKEN, anchor="w")
        self.connect_status.pack(side=tk.BOTTOM, fill=tk.X)
