from tkinter import Frame, Label, Entry
from tkinter.ttk import Button

import requests


class Registration(Frame):
    def __init__(self, master=None):
        super(Registration, self).__init__(master)

        self.header_label = Label(self, text="\nРегистрация", font=('Helvetica', 18, "bold"))
        self.header_label.pack()

        self.email_label = Label(self, text="\n\nЭлектронная почта", font=('Helvetica', 12))
        self.email_label.pack()

        self.email_entry = Entry(self)
        self.email_entry.pack()

        self.username_label = Label(self, text="\nИмя пользователя", font=('Helvetica', 12))
        self.username_label.pack()

        self.username_entry = Entry(self)
        self.username_entry.pack()

        self.password_label = Label(self, text="\nПароль", font=('Helvetica', 12))
        self.password_label.pack()

        self.password_entry = Entry(self)
        self.password_entry.pack()

        self.sign_up_button = Button(self, text="Зарегистрироваться", command=self.registration)
        self.sign_up_button.pack(pady=20)

    def registration(self):
        reply = requests.post('http://localhost:23432/auth/sign-up/', json={
            "email": self.email_entry.get(),
            "username": self.username_entry.get(),
            "password": self.password_entry.get()
        })

        if reply.status_code == requests.codes.ok:
            self.master.switch_frame(self.master.login_page)

