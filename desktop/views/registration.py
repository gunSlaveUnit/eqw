from tkinter import Frame, Label, Entry
from tkinter.ttk import Button
import requests


from desktop.materials.strings import REGISTRATION_LABEL, EMAIL_LABEL, USER_NAME_LABEL, PASSWORD_LABEL, \
    REGISTRATION_BUTTON


class Registration(Frame):
    def __init__(self, master=None):
        super(Registration, self).__init__(master)
        master=master

        self.header_label = Label(self, text=REGISTRATION_LABEL, font=('Helvetica', 12, "bold"), pady=15)
        self.header_label.pack()

        self.email_label = Label(self, text=EMAIL_LABEL, font=('Helvetica', 12), pady=30)
        self.email_label.pack()

        self.email_entry = Entry(self)
        self.email_entry.pack()

        self.username_label = Label(self, text=USER_NAME_LABEL, font=('Helvetica', 12), pady=15)
        self.username_label.pack()

        self.username_entry = Entry(self)
        self.username_entry.pack()

        self.password_label = Label(self, text=PASSWORD_LABEL, font=('Helvetica', 12))
        self.password_label.pack()

        self.password_entry = Entry(self)
        self.password_entry.pack()

        self.sign_up_button = Button(self, text=REGISTRATION_BUTTON, command=self.registration)
        self.sign_up_button.pack(pady=20)

    def registration(self):
        reply = requests.post('http://localhost:23432/auth/sign-up/', json={
            "email": self.email_entry.get(),
            "username": self.username_entry.get(),
            "password": self.password_entry.get()
        })

        if reply.status_code == requests.codes.ok:
            self.master.switch_frame(self.master.login_page)

