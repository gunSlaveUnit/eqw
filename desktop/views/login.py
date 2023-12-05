from tkinter import Frame, Label, Entry
from tkinter.ttk import Button

import requests

from desktop.materials.strings import LOGIN_LABEL, LOGIN_BUTTON, PASSWORD_LABEL, USER_NAME_LABEL, GO_TO_AUTH_LABEL, \
    EMAIL_LABEL
from desktop.settings import LOGIN_URL


class Login(Frame):
    def __init__(self, master=None):
        super(Login, self).__init__(master)

        self.master = master

        self.header_label = Label(self, text=LOGIN_LABEL, font=('Helvetica', 18, "bold"))
        self.header_label.pack(pady=20)

        self.username_label = Label(self, text=EMAIL_LABEL, font=('Helvetica', 12), pady=30)
        self.username_label.pack()

        self.username_entry = Entry(self)
        self.username_entry.pack()

        self.password_label = Label(self, text=PASSWORD_LABEL, font=('Helvetica', 12), pady=15)
        self.password_label.pack()

        self.password_entry = Entry(self)
        self.password_entry.pack()

        self.login_button = Button(self, text=LOGIN_BUTTON, command=self.login)
        self.login_button.pack(pady=20)

        def auth(self):
            master.switch_frame(master.registration_page)

        self.auth_label = Label(self, text=GO_TO_AUTH_LABEL, font=('Helvetica', 12), pady=15, )
        self.auth_label.bind("<Button-1>", auth)
        self.auth_label.pack()



    def login(self):
        reply = requests.post(LOGIN_URL, json={
            "email": self.username_entry.get(),
            "password": self.password_entry.get()
        })

        if reply.status_code == requests.codes.ok:
            self.master.authorized_session = requests.session()
            self.master.authorized_session.cookies.set('session', reply.cookies["session"])
            self.master.load_current_user()
            self.master.switch_frame(self.master.menu_page)
            self.master.full_ui()

