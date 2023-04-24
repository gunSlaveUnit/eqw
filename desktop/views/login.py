from tkinter import Frame, Label, Entry
from tkinter.ttk import Button

import requests

from desktop.materials.strings import LOGIN_LABEL, LOGIN_BUTTON, PASSWORD_LABEL, USER_NAME_LABEL


class Login(Frame):
    def __init__(self, master=None):
        super(Login, self).__init__(master)

        self.master = master

        self.header_label = Label(self, text=LOGIN_LABEL, font=('Helvetica', 18, "bold"))
        self.header_label.pack(pady=20)

        self.username_label = Label(self, text=USER_NAME_LABEL, font=('Helvetica', 12), pady=30)
        self.username_label.pack()

        self.username_entry = Entry(self)
        self.username_entry.pack()

        self.password_label = Label(self, text=PASSWORD_LABEL, font=('Helvetica', 12), pady=15)
        self.password_label.pack()

        self.password_entry = Entry(self)
        self.password_entry.pack()

        self.login_button = Button(self, text=LOGIN_BUTTON, command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        reply = requests.post('http://localhost:23432/auth/sign-in/', json={
            "username": self.username_entry.get(),
            "password": self.password_entry.get()
        })

        if reply.status_code == requests.codes.ok:
            self.master.switch_frame(self.master.menu_page)
            self.master.full_ui()
