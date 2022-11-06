try:
   # for Python2
   from Tkinter import *
except ImportError:
   # for Python3
   from tkinter import *

class   Application(Frame):
    def __init__(self,  master=None):
        Frame.__init__(self, master)
        self.grid(sticky=N+S+E+W)
        self.mainframe()

    def mainframe(self):
       frame = Frame(self)
       scrollbar = Scrollbar(frame, orient=VERTICAL)
       data = Listbox(frame, yscrollcommand=scrollbar.set,
              bg='red')
       scrollbar.config(command=data.yview)
       scrollbar.pack(side=RIGHT, fill=Y)
       data.pack(side=LEFT, fill=BOTH, expand=1)

       for i in range(1000):
          data.insert(END, str(i))

       self.run = Button(self, text="run")
       self.stop = Button(self, text="stop")

       frame.grid(row=0, column=0, rowspan=4,
                   columnspan=2, sticky=N+E+S+W)
       frame.columnconfigure(0, weight=1)

       self.run.grid(row=4,column=0,sticky=EW)
       self.stop.grid(row=4,column=1,sticky=EW)

a = Application()
a.mainframe()
a.mainloop()
