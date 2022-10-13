from tkinter import Tk, BOTTOM, LEFT, HORIZONTAL, Listbox, BOTH, Label
from tkinter.ttk import Style, Frame, Button, Entry, PanedWindow

root = Tk()
root.title('PanedWindow Demo')
root.geometry('400x300')

style = Style()
style.theme_use('classic')

connect_frame = Frame(root)
connect_frame.pack()

text_broker = Label(connect_frame, text="Broker:")
text_broker.pack(side=LEFT)

entry_broker = Entry(connect_frame)
entry_broker.pack(side=LEFT)

pw = PanedWindow(orient=HORIZONTAL)

B1 = Button(root, text="show")
B1.pack()
pw.add(B1)

right_list = Listbox(root)
right_list.pack(side=LEFT)
pw.add(right_list)

pw.pack(fill=BOTH, expand=True)

root.mainloop()
