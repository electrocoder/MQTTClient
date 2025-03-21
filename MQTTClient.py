"""
MQTT Client GUI - Main Application
Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>
Source Code: https://github.com/electrocoder/MQTTClient
MQTT Examples: https://github.com/mesebilisim/mqtt-examples
Date: Updated on March 22, 2025
"""

import os
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from about import AboutWindow
from config_file import ConfigFile
from subscriber import Subscriber
from new_connect import NewConnect
from new_topic import NewTopic


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('MQTT Client 0v5')
        self.geometry('800x500')
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12))
        self.style.configure("TLabel", font=("Helvetica", 12))

        self.msg_filter = False
        self.subscriber = Subscriber(self)
        self._setup_ui()

    def _setup_ui(self):
        self.main_frame = ttk.Frame(self, padding="10")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self._create_broker_section()
        self._create_publish_section()
        self._create_subscribe_section()
        self._create_filter_section()
        self._create_message_list()
        self._create_menu()
        self._create_status_bar()

        # Load icon if exists
        basedir = os.path.dirname(__file__)
        icon_path = os.path.join(basedir, "icon.png")
        if os.path.exists(icon_path):
            photo = tk.PhotoImage(file=icon_path)
            self.wm_iconphoto(False, photo)

    def _create_broker_section(self):
        broker_frame = ttk.LabelFrame(self.main_frame, text="Broker", padding="5")
        broker_frame.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        ttk.Label(broker_frame, text="Broker:").grid(row=0, column=0, padx=5)
        self.entry_broker_text = tk.StringVar(value="Select Broker")
        self.entry_broker = ttk.OptionMenu(broker_frame, self.entry_broker_text, "Select Broker", *ConfigFile().read_sections())
        self.entry_broker.grid(row=0, column=1, padx=5, sticky="ew")

        self.button_connect = ttk.Button(broker_frame, text="Connect", command=self.button_connect)
        self.button_connect.grid(row=0, column=2, padx=5)
        self.button_disconnect = ttk.Button(broker_frame, text="Disconnect", command=self.button_disconnect, state="disabled")
        self.button_disconnect.grid(row=0, column=3, padx=5)

    def _create_publish_section(self):
        publish_frame = ttk.LabelFrame(self.main_frame, text="Publish", padding="5")
        publish_frame.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        ttk.Label(publish_frame, text="Topic:").grid(row=0, column=0, padx=5)
        self.entry_publish_topic_text = tk.StringVar()
        ttk.Entry(publish_frame, textvariable=self.entry_publish_topic_text).grid(row=0, column=1, padx=5, sticky="ew")

        ttk.Label(publish_frame, text="Message:").grid(row=0, column=2, padx=5)
        self.entry_publish_msg_text = tk.StringVar()
        ttk.Entry(publish_frame, textvariable=self.entry_publish_msg_text).grid(row=0, column=3, padx=5, sticky="ew")

        self.button_publish = ttk.Button(publish_frame, text="Publish", command=self.button_publish_topic, state="disabled")
        self.button_publish.grid(row=0, column=4, padx=5)

    def _create_subscribe_section(self):
        subscribe_frame = ttk.LabelFrame(self.main_frame, text="Subscribe", padding="5")
        subscribe_frame.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        ttk.Label(subscribe_frame, text="Topic:").grid(row=0, column=0, padx=5)
        self.entry_subscribe_topic_text = tk.StringVar(value="-")
        self.entry_subscribe_topic = ttk.OptionMenu(subscribe_frame, self.entry_subscribe_topic_text, "-", "-", command=self.add_subscribe_topic)
        self.entry_subscribe_topic.grid(row=0, column=1, padx=5, sticky="ew")

        self.button_subscribe = ttk.Button(subscribe_frame, text="Subscribe", command=self.button_subscribe, state="disabled")
        self.button_subscribe.grid(row=0, column=2, padx=5)
        self.button_add_topic = ttk.Button(subscribe_frame, text="Add Topic", command=self.add_subscribe_topic, state="disabled")
        self.button_add_topic.grid(row=0, column=3, padx=5)

    def _create_filter_section(self):
        filter_frame = ttk.LabelFrame(self.main_frame, text="Filter Messages", padding="5")
        filter_frame.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        ttk.Label(filter_frame, text="Filter:").grid(row=0, column=0, padx=5)
        self.entry_msg_filter_text = tk.StringVar()
        ttk.Entry(filter_frame, textvariable=self.entry_msg_filter_text).grid(row=0, column=1, padx=5, sticky="ew")

        self.button_filter_add = ttk.Button(filter_frame, text="Add Filter", command=self.add_filter, state="disabled")
        self.button_filter_add.grid(row=0, column=2, padx=5)
        self.button_filter_remove = ttk.Button(filter_frame, text="Remove Filter", command=self.remove_filter, state="disabled")
        self.button_filter_remove.grid(row=0, column=3, padx=5)

    def _create_message_list(self):
        message_frame = ttk.LabelFrame(self.main_frame, text="Messages", padding="5")
        message_frame.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        self.main_frame.rowconfigure(4, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

        self.listbox_message = tk.Text(message_frame, font=("Helvetica", 12), height=10)
        self.listbox_message.pack(expand=True, fill="both")

    def _create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        menu_connect = tk.Menu(menubar, tearoff=0)
        menu_connect.add_command(label='New Connect', command=self.new_connect_window)
        menu_connect.add_separator()
        menu_connect.add_command(label='Exit', command=self.quit)
        menubar.add_cascade(label="Connect", menu=menu_connect)

        menu_help = tk.Menu(menubar, tearoff=0)
        menu_help.add_command(label='Help', command=self.help)
        menu_help.add_command(label='About', command=self.about_window)
        menubar.add_cascade(label="Help", menu=menu_help)

    def _create_status_bar(self):
        self.connect_status_text = tk.StringVar(value="Disconnected")
        self.status_bar = ttk.Label(self.main_frame, textvariable=self.connect_status_text, relief="sunken", anchor="w")
        self.status_bar.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

    def update_status(self, message):
        self.connect_status_text.set(message)
        self.status_bar.configure(background="green" if "Connected" in message else "red")

    def refresh_broker_list(self):
        menu = self.entry_broker["menu"]
        menu.delete(0, "end")
        brokers = ConfigFile().read_sections()
        for broker in brokers:
            menu.add_command(label=broker, command=lambda b=broker: self.entry_broker_text.set(b))
        if brokers:
            self.entry_broker_text.set(brokers[0])

    def refresh_subscribe_list(self):
        menu = self.entry_subscribe_topic["menu"]
        menu.delete(0, "end")
        topics = ConfigFile().read_topics(self.entry_broker_text.get()).split(',')
        for topic in topics:
            if topic:
                menu.add_command(label=topic, command=lambda t=topic: self.entry_subscribe_topic_text.set(t))
        if topics:
            self.entry_subscribe_topic_text.set(topics[0])

    def button_connect(self):
        if self.entry_broker_text.get() == "Select Broker":
            messagebox.showerror("Error", "Please select a broker.")
            return
        name, broker, port, username, password = ConfigFile().read_broker(self.entry_broker_text.get())
        if self.subscriber.connect_start(name, broker, port, username, password):
            self.button_connect.configure(state="disabled", text="Connected")
            self.button_disconnect.configure(state="normal")
            self.button_subscribe.configure(state="normal")
            self.button_publish.configure(state="normal")
            self.button_add_topic.configure(state="normal")
            self.button_filter_add.configure(state="normal")
            self.refresh_subscribe_list()

    def button_disconnect(self):
        if self.subscriber.connect_stop():
            self.update_status("Disconnected")
            self.button_connect.configure(state="normal", text="Connect")
            self.button_disconnect.configure(state="disabled")
            self.button_subscribe.configure(state="disabled")
            self.button_publish.configure(state="disabled")
            self.button_add_topic.configure(state="disabled")
            self.button_filter_add.configure(state="disabled")
            self.button_filter_remove.configure(state="disabled")

    def button_subscribe(self):
        self.subscriber.subscribe_start(self.entry_subscribe_topic_text.get())

    def button_publish_topic(self):
        topic = self.entry_publish_topic_text.get()
        msg = self.entry_publish_msg_text.get()
        if topic and msg:
            self.listbox_message.insert(tk.END, f"> {msg}\n")
            self.listbox_message.see("end")
            self.subscriber.publish_start(topic, msg)

    def about_window(self):
        AboutWindow(self)

    def help(self):
        webbrowser.open_new_tab("https://github.com/electrocoder/MQTTClient")

    def new_connect_window(self):
        NewConnect(self)

    def add_subscribe_topic(self, *args):
        NewTopic(self)

    def add_filter(self):
        self.msg_filter = True
        self.button_filter_add.configure(state="disabled")
        self.button_filter_remove.configure(state="normal")

    def remove_filter(self):
        self.msg_filter = False
        self.button_filter_add.configure(state="normal")
        self.button_filter_remove.configure(state="disabled")


if __name__ == "__main__":
    app = App()
    app.mainloop()
