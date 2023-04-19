from tkinter import Frame, Label, Entry
from tkinter.ttk import Button

import requests


class Login(Frame):
    def __init__(self, master=None):
        super(Login, self).__init__(master)

        self.header_label = Label(self, text="Вход")
        self.header_label.pack()

        self.username_label = Label(self, text="Имя пользователя")
        self.username_label.pack()

        self.username_entry = Entry(self)
        self.username_entry.pack()

        self.password_label = Label(self, text="Пароль")
        self.password_label.pack()

        self.password_entry = Entry(self)
        self.password_entry.pack()

        self.login_button = Button(self, text="Войти", command=self.login)
        self.login_button.pack()

    def login(self):
        reply = requests.post('http://localhost:23432/auth/sign-in/', json={
            "username": self.username_entry.get(),
            "password": self.password_entry.get()
        })

        if reply.status_code == requests.codes.ok:
            pass
