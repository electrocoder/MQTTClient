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

        # publich topic
        self.label_publich_topic = tk.Label(self, text="Publish Topic")
        self.label_publich_topic.grid(row=row, column=column)

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
                                              text="Publich",
                                              command=main_window_self.button_publish_topic)
        self.button_publich_topic.grid(row=row, column=column)

        row += 1
        column = 1

        # publish list
        self.listbox_publish_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.listbox_publish = tk.Listbox(self, width=20, height=10)
        self.listbox_publish.config(yscrollcommand=self.listbox_publish_scrollbar.set)
        self.listbox_publish.grid(row=row, column=column)
        self.listbox_publish_scrollbar.config(command=self.listbox_publish.yview)
        self.listbox_publish_scrollbar.grid(row=row, column=column+1, sticky='ns')

        column = 0
        row += 1

        # subscribe topic
        self.label_subscribe_topic = tk.Label(self, text="Subscribe Topic")
        self.label_subscribe_topic.grid(row=row, column=column)

        column += 1
        self.entry_subscribe_topic_text = tk.StringVar(self)
        self.entry_subscribe_topic = tk.Entry(self,
                                              textvariable=self.entry_subscribe_topic_text)
        self.entry_subscribe_topic.grid(row=row, column=column)

        column += 1
        self.button_subscribe_topic = tk.Button(self,
                                                text="Subscribe",
                                                command=main_window_self.button_subscribe_topic)
        self.button_subscribe_topic.grid(row=row, column=column)

        row += 1
        column = 1

        # subscribe list
        self.listbox_subscribe_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.listbox_subscribe = tk.Listbox(self, width=20, height=10)
        self.listbox_subscribe.config(yscrollcommand=self.listbox_subscribe_scrollbar.set)
        self.listbox_subscribe.grid(row=row, column=column)
        self.listbox_subscribe_scrollbar.config(command=self.listbox_subscribe.yview)
        self.listbox_subscribe_scrollbar.grid(row=row, column=column+1, sticky='ns')

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
        menu_help.add_command(label='About',
                              command=self.main_window_self.about_window)
        menubar.add_cascade(label="Help", menu=menu_help)

        # status bar
        self.status_text = tk.StringVar()
        self.status_text.set("...")
        self.status = tk.Label(main_window_self, textvariable=self.status_text,
                               relief=tk.SUNKEN, anchor="w")
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
