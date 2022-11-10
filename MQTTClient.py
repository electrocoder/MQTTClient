import tkinter as tk
import webbrowser
from tkinter import messagebox

import paho.mqtt.client as mqtt

import about as about
import new_connect as new_connect
import open_connect as open_connect
import search as search
import subscriber
from config_file import ConfigFile
from main_window_frame_ui import MainWindowFrameUI


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('MQTT Client')
        self.geometry('700x300')

        self.main_window_frame = tk.Frame()
        self.main_window_frame.pack()

        self.main_window_frame_ui = MainWindowFrameUI(self.main_window_frame,
                                                      self, height=35)
        self.main_window_frame_ui.pack()

        self.sub = subscriber.Subscriber(self.main_window_frame_ui,
                                         mqtt.Client())

    def button_connect(self):
        print("button_connect")
        if self.main_window_frame_ui.entry_broker_text.get():
            broker, port, username, password = ConfigFile().read_broker(
                self.main_window_frame_ui.entry_broker_text.get())
            print(broker, port, username, password)
            if self.sub.connect_start(broker, port, username, password):
                self.main_window_frame_ui.connect_status_text.set("Connected")
                self.main_window_frame_ui.button_connect["state"] = tk.DISABLED
                self.main_window_frame_ui.button_connect["text"] = "Connected"
                self.main_window_frame_ui.button_disconnect[
                    "state"] = tk.NORMAL
                self.main_window_frame_ui.button_subscribe_topic[
                    "state"] = tk.NORMAL
                self.main_window_frame_ui.button_publich_topic[
                    "state"] = tk.NORMAL
                self.main_window_frame_ui.button_search[
                    "state"] = tk.NORMAL
        else:
            messagebox.showerror("showerror", "Please select broker.")

    def button_disconnect(self):
        print("button_disconnect")
        if self.sub.connect_stop():
            self.main_window_frame_ui.connect_status_text.set("Disconnect")
            self.main_window_frame_ui.button_connect["state"] = tk.NORMAL
            self.main_window_frame_ui.button_connect["text"] = "Connect"
            self.main_window_frame_ui.button_disconnect["state"] = tk.DISABLED
            self.main_window_frame_ui.button_subscribe_topic[
                "state"] = tk.DISABLED
            self.main_window_frame_ui.button_publich_topic[
                "state"] = tk.DISABLED

    def button_subscribe_topic(self):
        print("button_subscribe_topic")
        self.sub.subscribe_start(
            self.main_window_frame_ui.entry_subscribe_topic_text.get())
    def search(self):
        print("search")
        search.SearchWindow(self.master)

    def button_publish_topic(self):
        print("button_publish_topic")
        topic = self.main_window_frame_ui.entry_publich_topic_text.get()
        msg = self.main_window_frame_ui.entry_publich_topic_msg_text.get()
        self.main_window_frame_ui.listbox_message.insert(tk.END,
                                                         "> {}".format(msg))
        self.main_window_frame_ui.listbox_message.see("end")
        self.sub.publish_start(topic, msg)

    def about_window(self):
        about.AboutWindow(self.master)

    def help(self):
        webbrowser.open_new_tab("https://github.com/electrocoder/MQTTClient")

    def new_connect_window(self):
        new_connect.NewConnect(self.master)

    def open_connect_window(self):
        open_connect.OpenConnect(self.main_window_frame_ui)


if __name__ == "__main__":
    app = App()

    photo = tk.PhotoImage(file='icon.png')
    app.wm_iconphoto(False, photo)

    app.mainloop()
