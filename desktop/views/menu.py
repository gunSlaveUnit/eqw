from tkinter import Frame, Label


class Menu(Frame):
    def __init__(self, master=None):
        super(Menu, self).__init__(master)

        header_label = Label(self, text="Меню")
        header_label.pack()
