"""from PySide6.QtWidgets import QApplication, QLabel, QStackedWidget, QMainWindow


# TODO: maybe we need two windows: one when user is not registered and one when it is
from desktop.config.config import PAGE
from desktop.materials.menu import Menu
from desktop.views.info import InfoPage
from desktop.views.login import SignInPage
from desktop.views.registration import SignUpPage


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        # Pages
        self.sign_in_page = SignInPage(self)
        self.sign_up_page = SignUpPage(self)
        self.info_page = None
        self.menu = None



        self.central_widget = QStackedWidget()

        self.set_cropped_ui()

    def set_cropped_ui(self):
        # Window
        self.setWindowTitle("WINDOW_TITLE")
        self.setBaseSize(800, 600)

        # Pages
        self.central_widget.insertWidget(PAGE.SIGN_UP.value, self.sign_up_page)
        self.central_widget.insertWidget(PAGE.SIGN_IN.value, self.sign_in_page)

        self.central_widget.setCurrentIndex(PAGE.SIGN_IN.value)

        self.setCentralWidget(self.central_widget)

    def set_full_ui(self):
        self.info_page = InfoPage(self)

        self.menu = Menu(self)

        self.central_widget.insertWidget(PAGE.INFO.value, self.info_page)

        self.setMenuBar(self.menu)



    def change_page(self, index):
        # TODO: maybe it's good to update this page here
        self.central_widget.setCurrentIndex(index)

def main():
    app = QApplication()

    window = Window()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()

"""
from tkinter.ttk import Notebook

import ttkbootstrap

from ttkbootstrap import Window

from desktop.views.check import Check
from desktop.views.info import Info
from desktop.views.menu import Menu
from desktop.views.registration import Registration
from views.login import Login


class MainWindow(Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        ttkbootstrap.Style().theme_use('vapor')
        self.login_page = Login(self)
        self.registration_page = Registration(self)
        self.menu_page = Menu(self)
        self.current_frame = self.login_page
        self.current_frame.pack()



    def switch_frame(self, frame):
        self.current_frame.destroy()
        self.current_frame = frame
        self.current_frame.pack()

    def full_ui(self, tk=None):
        
 
        notebook = Notebook(self)
        notebook.pack(pady=10, expand=True)

        frame1 = Info(notebook)
        frame2 = Check(notebook)
        frame3 = tk.Frame(notebook, width=780, height=580)

        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)
        frame3.pack(fill='both', expand=True)

        notebook.add(frame1, text='Tab 1')
        notebook.add(frame2, text='Tab 2')
        notebook.add(frame3, text='Справка')



main_window = MainWindow()
main_window.title("Проверка трафика")
main_window.geometry('800x600')
main_window.resizable(width=0, height=0)
main_window.mainloop()