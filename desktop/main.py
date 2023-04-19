from ttkbootstrap import Window

from desktop.views.menu import Menu
from desktop.views.registration import Registration
from views.login import Login


class MainWindow(Window):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.login_page = Login(self)
        self.registration_page = Registration(self)
        self.menu_page = Menu(self)

        self.current_frame = self.login_page
        self.current_frame.pack()

    def switch_frame(self, frame):
        self.current_frame.destroy()
        self.current_frame = frame
        self.current_frame.pack()


main_window = MainWindow()
main_window.title("Проверка трафика")
main_window.geometry('400x300')
main_window.mainloop()
