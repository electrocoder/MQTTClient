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

import paho.mqtt.client as mqtt

import about as about
import new_connect as new_connect
import open_connect as open_connect
import new_topic as new_topic
import subscriber
from config_file import ConfigFile
from main_window_frame_ui import MainWindowFrameUI


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('MQTT Client 0v3')
        self.geometry('850x450')

        self.text_font = Font(size=12)

        # self.main_window_frame = tk.Frame()
        # self.main_window_frame.pack()

        # self.main_window_frame_ui = MainWindowFrameUI(self.main_window_frame,
        #                                               self,
        #                                               font_size=self.text_font)
        # self.main_window_frame_ui.pack()

        font_size = 14

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
                                              command=self.button_publish_topic)
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
        options_list = ["New", "qqq"]
        self.entry_subscribe_topic = tk.OptionMenu(self,
                                                   self.entry_subscribe_topic_text,
                                                   *options_list, command=None)
        # menu_connect.add_command(label='New Connect',
        #                          command=self.main_window_self.new_connect_window)
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
                                                command=self.button_subscribe_topic)
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
        self.listbox_message = tk.Text(self, font=font_size, height=12)
        self.listbox_message.grid(row=row, column=column, columnspan=6,
                                  ipadx=11, ipady=11, padx=22, pady=22)

        # menu
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        menu_connect = tk.Menu(menubar, tearoff=0)
        menu_connect.add_command(label='New Connect',
                                 command=self.new_connect_window)
        menu_connect.add_command(label='Open Connect',
                                 command=self.open_connect_window)
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
                                       relief=tk.SUNKEN, anchor="w")
        row += 1
        column = 0

        self.connect_status.grid(row=row, column=column)

        # self.subscriber = subscriber.Subscriber(self.main_window_frame_ui,
        #                                         mqtt.Client())

    def button_connect(self):
        print("button_connect")
        if self.entry_broker_text.get():
            broker, port, username, password = ConfigFile().read_broker(
                self.entry_broker_text.get())
            print(broker, port, username, password)
            if self.subscriber.connect_start(broker, port, username, password):
                self.connect_status_text.set("Connected")
                self.button_connect["state"] = tk.DISABLED
                self.button_connect["text"] = "Connected"
                self.button_disconnect[
                    "state"] = tk.NORMAL
                self.button_subscribe_topic[
                    "state"] = tk.NORMAL
                self.button_publich_topic[
                    "state"] = tk.NORMAL
                topics = ConfigFile().read_topics(
                    self.entry_broker_text.get())
                print(topics)
        else:
            messagebox.showerror("showerror", "Please select broker.")

    def button_disconnect(self):
        print("button_disconnect")
        if self.subscriber.connect_stop():
            self.connect_status_text.set("Disconnect")
            self.button_connect["state"] = tk.NORMAL
            self.button_connect["text"] = "Connect"
            self.button_disconnect["state"] = tk.DISABLED
            self.button_subscribe_topic[
                "state"] = tk.DISABLED
            self.button_publich_topic[
                "state"] = tk.DISABLED

    def button_subscribe_topic(self):
        print("button_subscribe_topic")
        self.subscriber.subscribe_start(
            self.entry_subscribe_topic_text.get())
        self.button_filter_add[
            "state"] = tk.NORMAL
        self.button_filter_remove[
            "state"] = tk.DISABLED


    def button_publish_topic(self):
        print("button_publish_topic")
        topic = self.entry_publich_topic_text.get()
        msg = self.entry_publich_topic_msg_text.get()
        self.listbox_message.insert(tk.END,
                                                         "> {}".format(msg))
        self.listbox_message.see("end")
        self.subscriber.publish_start(topic, msg)

    def about_window(self):
        about.AboutWindow(self.master, self.text_font)

    def help(self):
        webbrowser.open_new_tab("https://github.com/electrocoder/MQTTClient")

    def new_connect_window(self):
        new_connect.NewConnect(self.master, self.text_font)

    def new_topic_window(self):
        new_topic.NewTopic(self.master, self.text_font)

    def open_connect_window(self):
        open_connect.OpenConnect(self, self.text_font)

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
