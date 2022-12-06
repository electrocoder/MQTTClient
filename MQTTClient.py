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

import about
import new_connect
import new_topic
import subscriber
from config_file import ConfigFile


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('MQTT Client 0v4')
        self.geometry('750x350')

        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)

        ipadding = {'ipadx': 10, 'ipady': 10}

        frame = tk.Frame(self)
        frame.pack(fill = tk.BOTH, expand = True)

        font_size = 14
        self.text_font = Font(size=font_size)

        self.msg_filter = False

        self.label_broker = tk.Label(frame, text="Broker", font=font_size)
        self.label_broker.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.entry_broker_text = tk.StringVar(self)
        self.options_list = ConfigFile().read_sections()
        self.entry_broker_text.set(self.options_list[0])
        self.entry_broker = tk.OptionMenu(frame,
                                          self.entry_broker_text,
                                          *self.options_list)

        self.entry_broker.config(font=font_size)
        menu = self.nametowidget(
            self.entry_broker.menuname)
        menu.config(font=font_size)

        self.entry_broker.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.button_connect = tk.Button(frame,
                                        text="Connect", font=font_size,
                                        command=self.button_connect)
        self.button_connect.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.button_disconnect = tk.Button(frame,
                                           text="Disconnect", font=font_size,
                                           state=tk.DISABLED,
                                           command=self.button_disconnect)
        self.button_disconnect.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        frame1 = tk.Frame(self)
        frame1.pack(fill = tk.BOTH, expand = True)

        # publish topic
        self.label_publish_topic = tk.Label(frame1, text="Publish Topic",
                                            font=font_size)
        self.label_publish_topic.pack(**ipadding, expand=True, fill=tk.BOTH,
                                      side=tk.LEFT)

        self.entry_publish_topic_text = tk.StringVar(self)
        self.entry_publish_topic = tk.Entry(frame1,
                                            textvariable=self.entry_publish_topic_text,
                                            font=font_size)
        self.entry_publish_topic.pack(**ipadding, expand=True, fill=tk.BOTH,
                                      side=tk.LEFT)

        self.label_publish_msg_topic = tk.Label(frame1, text="Publish Message",
                                                font=font_size)
        self.label_publish_msg_topic.pack(**ipadding, expand=True,
                                          fill=tk.BOTH, side=tk.LEFT)

        self.entry_publish_topic_msg_text = tk.StringVar(self)
        self.entry_publish_msg_topic = tk.Entry(frame1,
                                                textvariable=self.entry_publish_topic_msg_text,
                                                font=font_size)
        self.entry_publish_msg_topic.pack(**ipadding, expand=True,
                                          fill=tk.BOTH, side=tk.LEFT)

        self.button_publish_topic = tk.Button(frame1,
                                              text="Publish", font=font_size,
                                              command=self.button_publish_topic)
        self.button_publish_topic.pack(**ipadding, expand=True, fill=tk.BOTH,
                                       side=tk.LEFT)

        frame2 = tk.Frame(self)
        frame2.pack(fill = tk.BOTH, expand = True)

        # subscribe topic
        self.label_subscribe_topic = tk.Label(frame2, text="Subscribe Topic",
                                              font=font_size)
        self.label_subscribe_topic.pack(**ipadding, expand=True, fill=tk.BOTH,
                                        side=tk.LEFT)

        self.entry_subscribe_topic_text = tk.StringVar(self)
        self.options_list = ["-", ]
        self.entry_subscribe_topic = tk.OptionMenu(frame2,
                                                   self.entry_subscribe_topic_text,
                                                   *self.options_list,
                                                   command=self.add_subscribe_topic)
        self.entry_subscribe_topic.config(font=font_size)
        menu = self.nametowidget(
            self.entry_subscribe_topic.menuname)
        menu.config(font=font_size)

        self.entry_subscribe_topic.pack(**ipadding, expand=True, fill=tk.BOTH,
                                        side=tk.LEFT)

        self.button_subscribe_topic = tk.Button(frame2,
                                                text="Subscribe",
                                                font=font_size,
                                                state=tk.DISABLED,
                                                command=self.button_subscribe)
        self.button_subscribe_topic.pack(**ipadding, expand=True, fill=tk.BOTH,
                                         side=tk.LEFT)

        self.button_add_subscribe_topic = tk.Button(frame2,
                                                    text="Add Subscribe Topic",
                                                    font=font_size,
                                                    state=tk.DISABLED,
                                                    command=self.add_subscribe_topic)
        self.button_add_subscribe_topic.pack(**ipadding, expand=True,
                                             fill=tk.BOTH, side=tk.LEFT)

        frame3 = tk.Frame(self)
        frame3.pack(fill = tk.BOTH, expand = True)

        # filter msg

        self.label_msg_filter = tk.Label(frame3, text="Filter Message",
                                         font=font_size)
        self.label_msg_filter.pack(**ipadding, expand=True, fill=tk.BOTH,
                                   side=tk.LEFT)

        self.entry_msg_filter_text = tk.StringVar(self)
        self.entry_msg_filter = tk.Entry(frame3,
                                         textvariable=self.entry_msg_filter_text,
                                         font=font_size)
        self.entry_msg_filter.pack(**ipadding, expand=True, fill=tk.BOTH,
                                   side=tk.LEFT)

        self.button_filter_add = tk.Button(frame3,
                                           text="Add Filter", font=font_size,
                                           state=tk.DISABLED,
                                           command=self.add_filter)
        self.button_filter_add.pack(**ipadding, expand=True, fill=tk.BOTH,
                                    side=tk.LEFT)

        self.button_filter_remove = tk.Button(frame3,
                                              text="Remove Filter",
                                              font=font_size,
                                              state=tk.DISABLED,
                                              command=self.remove_filter)
        self.button_filter_remove.pack(**ipadding, expand=True, fill=tk.BOTH,
                                       side=tk.LEFT)

        frame4 = tk.Frame(self)
        frame4.pack(fill = tk.BOTH, expand = True)

        # subscribe list
        self.listbox_message = tk.Text(frame4, font=font_size, height=10)
        self.listbox_message.pack(**ipadding, expand=True, fill=tk.BOTH,
                                  side=tk.LEFT)

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

        frame5 = tk.Frame(self)
        frame5.pack(fill = tk.BOTH, expand = True)

        # status bar
        self.connect_status_text = tk.StringVar()
        self.connect_status_text.set("...")
        self.connect_status = tk.Label(frame5,
                                       textvariable=self.connect_status_text,
                                       bd=1,
                                       relief=tk.SUNKEN, anchor=tk.W)

        self.connect_status.pack(**ipadding)

        self.subscriber = subscriber.Subscriber(self)

    def button_connect(self):
        if self.entry_broker_text.get():
            name, broker, port, username, password = ConfigFile().read_broker(
                self.entry_broker_text.get())
            if self.subscriber.connect_start(name, broker, port, username,
                                             password):
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
