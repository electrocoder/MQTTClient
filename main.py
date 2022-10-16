from tkinter import Tk, BOTTOM, LEFT, HORIZONTAL, Listbox, BOTH, Label
from tkinter.ttk import Style, Frame, Button, Entry, PanedWindow

root = Tk()
root.title('MQTT Client')
root.geometry('900x500')
style = Style()
style.theme_use('classic')

connect_frame = Frame(root)
connect_frame.pack()

text_broker = Label(connect_frame, text="Broker:")
text_broker.pack(side=LEFT)
entry_broker = Entry(connect_frame)
entry_broker.pack(side=LEFT)

text_username = Label(connect_frame, text="Username:")
text_username.pack(side=LEFT)
entry_username = Entry(connect_frame)
entry_username.pack(side=LEFT)

text_pass = Label(connect_frame, text="Password:")
text_pass.pack(side=LEFT)
entry_pass = Entry(connect_frame)
entry_pass.pack(side=LEFT)

button_connect = Button(connect_frame, text="Connect")
button_connect.pack(side=LEFT)


pw = PanedWindow(orient=HORIZONTAL)

button = Button(root, text="show")
button.pack()
pw.add(button)

listbox = Listbox(root)
listbox.pack(side=LEFT)
pw.add(listbox)

pw.pack(fill=BOTH, expand=True)

root.mainloop()
