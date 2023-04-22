"""from PySide6.QtWidgets import QWidget, QLineEdit, QLabel


class InfoPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        # Widgets
        self.email = QLabel("Привет")

"""

from tkinter import Frame, Label, Menu

class Info(Frame):
    def __init__(self, master=None):
        super(Info, self).__init__(master)
        master = master


        header_label = Label(self, text="Информация")
        header_label.pack()

