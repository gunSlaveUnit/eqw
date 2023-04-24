
from tkinter import Frame, Label, Menu

from desktop.materials.strings import NAME


class Menu(Frame):
    def __init__(self, master=None):
        super(Menu, self).__init__(master)


        header_label = Label(self, text=NAME)
        header_label.pack()

