"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/mesebilisim/mqtt-examples

Date: 12.11.2022

File: This script is MQTT Client Main Application UI Design.
"""

import tkinter as tk

from config_file import ConfigFile


class MainWindowFrameUI(tk.Frame):
    def __init__(self, main_window_frame, main_window_self, font_size, *args,
                 **kwargs):
        super().__init__(master=main_window_frame, *args, **kwargs)

        self.main_window_frame = main_window_frame
        self.main_window_self = main_window_self

        self.msg_filter = False

        row = 0
        column = 0

        self.label_broker = tk.Label(self, text="Broker", font=font_size)
        self.label_broker.grid(row=row, column=column, sticky=tk.W)
        column += 1

        self.entry_broker_text = tk.StringVar(self)
        self.entry_broker = tk.Entry(self, textvariable=self.entry_broker_text,
                                     font=font_size)
        self.entry_broker.grid(row=row, column=column)

        column += 1

        self.button_connect = tk.Button(self,
                                        text="Connect", font=font_size,
                                        command=main_window_self.button_connect)
        self.button_connect.grid(row=row, column=column)

        column += 1

        self.button_disconnect = tk.Button(self,
                                           text="Disconnect", font=font_size,
                                           state=tk.DISABLED,
                                           command=main_window_self.button_disconnect)
        self.button_disconnect.grid(row=row, column=column, sticky=tk.W)

        row += 1
        column = 0

        # publich topic
        self.label_publich_topic = tk.Label(self, text="Publish Topic",
                                            font=font_size)
        self.label_publich_topic.grid(row=row, column=column, sticky=tk.W)

        column += 1
        self.entry_publich_topic_text = tk.StringVar(self)
        self.entry_publich_topic = tk.Entry(self,
                                            textvariable=self.entry_publich_topic_text,
                                            font=font_size)
        self.entry_publich_topic.grid(row=row, column=column)

        column += 1
        self.label_publich_msg_topic = tk.Label(self, text="Publish Message",
                                                font=font_size)
        self.label_publich_msg_topic.grid(row=row, column=column)

        column += 1
        self.entry_publich_topic_msg_text = tk.StringVar(self)
        self.entry_publich_msg_topic = tk.Entry(self,
                                                textvariable=self.entry_publich_topic_msg_text,
                                                font=font_size)
        self.entry_publich_msg_topic.grid(row=row, column=column)

        column += 1
        self.button_publich_topic = tk.Button(self,
                                              text="Publish", font=font_size,
                                              command=main_window_self.button_publish_topic)
        self.button_publich_topic.grid(row=row, column=column)

        row += 1
        column = 0

        # subscribe topic
        self.label_subscribe_topic = tk.Label(self, text="Subscribe Topic",
                                              font=font_size)
        self.label_subscribe_topic.grid(row=row, column=column, sticky=tk.W)
        self.label_subscribe_topic.grid(row=row, column=column, sticky=tk.W)

        column += 1
        self.entry_subscribe_topic_text = tk.StringVar(self)
        options_list = ["New",]
        self.entry_subscribe_topic = tk.OptionMenu(self, self.entry_subscribe_topic_text,
                                          *options_list, command=self.main_window_self.new_topic_window)
        self.entry_subscribe_topic.config(font=font_size)
        menu = self.nametowidget(
            self.entry_subscribe_topic.menuname)
        menu.config(font=font_size)

        self.entry_subscribe_topic.grid(row=row, ipadx=55, column=column)

        column += 1
        self.button_subscribe_topic = tk.Button(self,
                                                text="Subscribe",
                                                font=font_size,
                                                state=tk.DISABLED,
                                                command=main_window_self.button_subscribe_topic)
        self.button_subscribe_topic.grid(row=row, column=column)

        # filter msg
        row += 1
        column = 0

        self.label_msg_filter = tk.Label(self, text="Filter Message",
                                         font=font_size)
        self.label_msg_filter.grid(row=row, column=column, sticky=tk.W)
        self.label_msg_filter.grid(row=row, column=column, sticky=tk.W)

        column += 1

        self.entry_msg_filter_text = tk.StringVar(self)
        self.entry_msg_filter = tk.Entry(self,
                                         textvariable=self.entry_msg_filter_text,
                                         font=font_size)
        self.entry_msg_filter.grid(row=row, column=column)
        column += 1

        self.button_filter_add = tk.Button(self,
                                           text="Add Filter", font=font_size,
                                           state=tk.DISABLED,
                                           command=main_window_self.add_filter)
        self.button_filter_add.grid(row=row, column=column)
        column += 1

        self.button_filter_remove = tk.Button(self,
                                              text="Remove Filter",
                                              font=font_size,
                                              state=tk.DISABLED,
                                              command=main_window_self.remove_filter)
        self.button_filter_remove.grid(row=row, column=column)

        row += 1
        column = 0

        # subscribe list
        self.listbox_message = tk.Text(self, font=font_size, height=12)
        self.listbox_message.grid(row=row, column=column, columnspan=6, ipadx=11, ipady=11, padx=22, pady=22)

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
