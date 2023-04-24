from tkinter import Frame, Label, Menu

class Settings(Frame):
    def __init__(self, master=None):
        super(Settings, self).__init__(master)
        master = master


        header_label = Label(self, text="Настройки")
        header_label.pack()

