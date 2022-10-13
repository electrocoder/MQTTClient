from tkinter import Tk, BOTTOM, LEFT, HORIZONTAL, Listbox, BOTH
from tkinter.ttk import Style, Frame, Button, Entry, PanedWindow

root = Tk()
root.title('PanedWindow Demo')
root.geometry('300x200')

style = Style()
style.theme_use('classic')

connect_frame = Frame(root)
connect_frame.pack()

redbutton = Button(connect_frame, text="Red")
redbutton.pack(side=LEFT)

E1 = Entry(connect_frame)
E1.pack()

pw = PanedWindow(orient=HORIZONTAL)

B1 = Button(root, text="show")
B1.pack()
pw.add(B1)

right_list = Listbox(root)
right_list.pack(side=LEFT)
pw.add(right_list)

pw.pack(fill=BOTH, expand=True)

root.mainloop()
