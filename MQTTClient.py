"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/mesebilisim/mqtt-examples

Date: 12.11.2022

File: This script is MQTT Client Main Application
"""
import os
import tkinter as tk
import webbrowser
from tkinter import messagebox
from tkinter.font import Font

import new_connect
import new_topic
import subscriber
import about

from config_file import ConfigFile


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('MQTT Client 0v4')
        self.geometry('750x350')

        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)

        font_size = 14
        self.text_font = Font(size=font_size)

        self.msg_filter = False
        row = 0
        column = 0

        self.label_broker = tk.Label(self, text="Broker", font=font_size)
        self.label_broker.grid(row=row, column=column, sticky=tk.W)
        column += 1

        self.entry_broker_text = tk.StringVar(self)
        self.options_list = ConfigFile().read_sections()
        self.entry_broker_text.set(self.options_list[0])
        self.entry_broker = tk.OptionMenu(self,
                                          self.entry_broker_text,
                                          *self.options_list)

        self.entry_broker.config(font=font_size)
        menu = self.nametowidget(
            self.entry_broker.menuname)
        menu.config(font=font_size)

        self.entry_broker.grid(row=row, column=column)

        column += 1

        self.button_connect = tk.Button(self,
                                        text="Connect", font=font_size,
                                        command=self.button_connect)
        self.button_connect.grid(row=row, column=column)

        column += 1

        self.button_disconnect = tk.Button(self,
                                           text="Disconnect", font=font_size,
                                           state=tk.DISABLED,
                                           command=self.button_disconnect)
        self.button_disconnect.grid(row=row, column=column, sticky=tk.W)

        row += 1
        column = 0

        # publish topic
        self.label_publish_topic = tk.Label(self, text="Publish Topic",
                                            font=font_size)
        self.label_publish_topic.grid(row=row, column=column, sticky=tk.W)

        column += 1
        self.entry_publish_topic_text = tk.StringVar(self)
        self.entry_publish_topic = tk.Entry(self,
                                            textvariable=self.entry_publish_topic_text,
                                            font=font_size)
        self.entry_publish_topic.grid(row=row, column=column)

        column += 1
        self.label_publish_msg_topic = tk.Label(self, text="Publish Message",
                                                font=font_size)
        self.label_publish_msg_topic.grid(row=row, column=column)

        column += 1
        self.entry_publish_topic_msg_text = tk.StringVar(self)
        self.entry_publish_msg_topic = tk.Entry(self,
                                                textvariable=self.entry_publish_topic_msg_text,
                                                font=font_size)
        self.entry_publish_msg_topic.grid(row=row, column=column)

        column += 1
        self.button_publish_topic = tk.Button(self,
                                              text="Publish", font=font_size,
                                              command=self.button_publish_topic)
        self.button_publish_topic.grid(row=row, column=column)

        row += 1
        column = 0

        # subscribe topic
        self.label_subscribe_topic = tk.Label(self, text="Subscribe Topic",
                                              font=font_size)
        self.label_subscribe_topic.grid(row=row, column=column, sticky=tk.W)

        column += 1
        self.entry_subscribe_topic_text = tk.StringVar(self)
        self.options_list = ["-", ]
        self.entry_subscribe_topic = tk.OptionMenu(self,
                                                   self.entry_subscribe_topic_text,
                                                   *self.options_list, command=self.add_subscribe_topic)
        self.entry_subscribe_topic.config(font=font_size)
        menu = self.nametowidget(
            self.entry_subscribe_topic.menuname)
        menu.config(font=font_size)

        self.entry_subscribe_topic.grid(row=row, column=column)

        column += 1
        self.button_subscribe_topic = tk.Button(self,
                                                text="Subscribe",
                                                font=font_size,
                                                state=tk.DISABLED,
                                                command=self.button_subscribe)
        self.button_subscribe_topic.grid(row=row, column=column)

        column += 1
        self.button_add_subscribe_topic = tk.Button(self,
                                                    text="Add Subscribe Topic",
                                                    font=font_size,
                                                    state=tk.DISABLED,
                                                    command=self.add_subscribe_topic)
        self.button_add_subscribe_topic.grid(row=row, column=column)

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
                                           command=self.add_filter)
        self.button_filter_add.grid(row=row, column=column)
        column += 1

        self.button_filter_remove = tk.Button(self,
                                              text="Remove Filter",
                                              font=font_size,
                                              state=tk.DISABLED,
                                              command=self.remove_filter)
        self.button_filter_remove.grid(row=row, column=column)

        row += 1
        column = 0

        # subscribe list
        self.listbox_message = tk.Text(self, font=font_size, height=10)
        self.listbox_message.grid(row=row, column=column, columnspan=6,
                                  ipadx=5, ipady=5, padx=5, pady=5)

        # menu
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        menu_connect = tk.Menu(menubar, tearoff=0)
        menu_connect.add_command(label='New Connect',
                                 command=self.new_connect_window)
        # menu_connect.add_command(label='Open Connect',
        #                          command=self.open_connect_window)
        menu_connect.add_separator()
        menu_connect.add_command(label='Exit', command=self.quit)
        menubar.add_cascade(label="Connect", menu=menu_connect)

        menu_help = tk.Menu(menubar, tearoff=0)
        menu_help.add_command(label='Help', command=self.help)
        menu_help.add_command(label='About',
                              command=self.about_window)
        menubar.add_cascade(label="Help", menu=menu_help)

        # status bar
        self.connect_status_text = tk.StringVar()
        self.connect_status_text.set("...")
        self.connect_status = tk.Label(self,
                                       textvariable=self.connect_status_text,
                                       bd=1,
                                       relief=tk.SUNKEN, anchor=tk.W)
        row += 1
        column = 0

        self.connect_status.grid(row=row, column=column, columnspan=5, sticky=tk.W+tk.E)

        self.subscriber = subscriber.Subscriber(self)

    def button_connect(self):
        if self.entry_broker_text.get():
            name, broker, port, username, password = ConfigFile().read_broker(
                self.entry_broker_text.get())
            if self.subscriber.connect_start(name, broker, port, username, password):
                self.connect_status_text.set("Connected")
                self.button_connect["state"] = tk.DISABLED
                self.button_connect["text"] = "Connected"
                self.button_disconnect[
                    "state"] = tk.NORMAL
                self.button_subscribe_topic[
                    "state"] = tk.NORMAL
                self.button_publish_topic[
                    "state"] = tk.NORMAL
                self.subscribe_list(name)
                self.button_add_subscribe_topic["state"] = tk.NORMAL
        else:
            messagebox.showerror("showerror", "Please select broker.")

    def subscribe_list(self, name):
        self.entry_subscribe_topic['menu'].delete(0, 'end')

        new_choices = ConfigFile().read_topics(name).split(',')
        for choice in new_choices:
            if choice:
                self.entry_subscribe_topic['menu'].add_command(
                    label=choice,
                    command=tk._setit(self.entry_subscribe_topic_text,
                                      choice))
                self.entry_subscribe_topic_text.set(choice)

    def button_disconnect(self):
        print("button_disconnect")
        if self.subscriber.connect_stop():
            self.connect_status_text.set("Disconnect")
            self.button_connect["state"] = tk.NORMAL
            self.button_connect["text"] = "Connect"
            self.button_disconnect["state"] = tk.DISABLED
            self.button_subscribe_topic[
                "state"] = tk.DISABLED
            self.button_publish_topic[
                "state"] = tk.DISABLED
            self.button_add_subscribe_topic["state"] = tk.DISABLED

    def button_subscribe(self):
        print("button_subscribe")
        self.subscriber.subscribe_start(
            self.entry_subscribe_topic_text.get())
        self.button_filter_add[
            "state"] = tk.NORMAL
        self.button_filter_remove[
            "state"] = tk.DISABLED

    def button_publish_topic(self):
        print("button_publish_topic")
        topic = self.entry_publish_topic_text.get()
        msg = self.entry_publish_topic_msg_text.get()
        self.listbox_message.insert(tk.END,
                                    "> {}".format(msg))
        self.listbox_message.see("end")
        self.subscriber.publish_start(topic, msg)

    def about_window(self):
        about.AboutWindow(self, self.text_font)

    def help(self):
        webbrowser.open_new_tab("https://github.com/electrocoder/MQTTClient")

    def new_connect_window(self):
        new_connect.NewConnect(self, self.text_font)

    def add_subscribe_topic(self, *args):
        print("add_subscribe_topic")
        new_topic.NewTopic(self, self.text_font)

    def add_filter(self):
        self.msg_filter = True
        self.button_filter_add[
            "state"] = tk.DISABLED
        self.button_filter_remove[
            "state"] = tk.NORMAL

    def remove_filter(self):
        self.msg_filter = False
        self.button_filter_add[
            "state"] = tk.NORMAL
        self.button_filter_remove[
            "state"] = tk.DISABLED


if __name__ == "__main__":
    app = App()

    basedir = os.path.dirname(__file__)
    file_name = os.path.join(basedir, "icon.png")
    photo = tk.PhotoImage(file=file_name)
    app.wm_iconphoto(False, photo)

    app.mainloop()
