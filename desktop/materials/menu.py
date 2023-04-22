from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar

from desktop.config.config import PAGE


class Menu(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        self.menu = QAction("LIBRARY_MENU_ACTION_TEXT")

        self.set_ui()

    def set_ui(self):
        self.menu.triggered.connect(lambda: self.parent.change_page(PAGE.MENU.value))

        self.addAction(self.menu)


