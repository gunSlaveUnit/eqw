"""import requests
from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton



class MenuPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent
        self.layout = QGridLayout()

        self.set_ui()

    def set_ui(self):
        self.button.setText("Меню")
        #self.add_game_button.clicked.connect(lambda: self.parent.change_page(PAGE.NEW_GAME.value))

        self.layout.addWidget(self.button)

"""

from tkinter import Frame, Label, Menu

class Menu(Frame):
    def __init__(self, master=None):
        super(Menu, self).__init__(master)


        header_label = Label(self, text="Меню")
        header_label.pack()

