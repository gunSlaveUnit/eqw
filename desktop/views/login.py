from tkinter import Frame, Label, Entry
from tkinter.ttk import Button

import requests


class Login(Frame):
    def __init__(self, master=None):
        super(Login, self).__init__(master)

        self.master = master

        self.header_label = Label(self, text="\nВход", font=('Helvetica', 18, "bold"))
        self.header_label.pack(pady=20)

        self.username_label = Label(self, text="\n\nИмя пользователя", font=('Helvetica', 12))
        self.username_label.pack()

        self.username_entry = Entry(self)
        self.username_entry.pack()

        self.password_label = Label(self, text="\nПароль\n", font=('Helvetica', 12))
        self.password_label.pack()

        self.password_entry = Entry(self)
        self.password_entry.pack()

        self.login_button = Button(self, text="Войти", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        reply = requests.post('http://localhost:23432/auth/sign-in/', json={
            "username": self.username_entry.get(),
            "password": self.password_entry.get()
        })

        if reply.status_code == requests.codes.ok:
            self.master.switch_frame(self.master.menu_page)
