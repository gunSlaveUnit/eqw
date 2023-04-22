
from tkinter import Frame, Label, Menu

class Check(Frame):
    def __init__(self, master=None):
        super(Check, self).__init__(master)
        master = master



        header_label = Label(self, text="Проверка")
        header_label.pack()

