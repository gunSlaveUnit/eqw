from tkinter import Frame, Label, Entry
from tkinter.ttk import Button


class Login(Frame):
    def __init__(self, master=None):
        super(Login, self).__init__(master)

        header_label = Label(self, text="Вход")
        header_label.pack()

        username_label = Label(self, text="Имя пользователя")
        username_label.pack()

        username_entry = Entry(self)
        username_entry.pack()

        password_label = Label(self, text="Пароль")
        password_label.pack()

        password_entry = Entry(self)
        password_entry.pack()

        login_button = Button(self, text="Войти")
        login_button.pack()
