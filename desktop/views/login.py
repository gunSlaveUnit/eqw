"""from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QLineEdit, QLabel

from desktop.config.config import PAGE


class SignInPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        # Widgets
        self.email = QLineEdit()
        self.password = QLineEdit()
        self.sign_in_button = QPushButton()
        self.no_account_label = QLabel()

        self.layout = QGridLayout()

        self.set_ui()

    def set_ui(self):
        self.password.setEchoMode(QLineEdit.Password)

        self.sign_in_button.setText("Войти")
        self.sign_in_button.clicked.connect(self.sign_in)

        self.no_account_label.setText("Нет аккаунта")
        self.no_account_label.mousePressEvent = self.no_account_label_pressed_event

        self.layout.addWidget(self.email)
        self.layout.addWidget(self.password)
        self.layout.addWidget(self.sign_in_button)
        self.layout.addWidget(self.no_account_label)

        self.setLayout(self.layout)

    def sign_in(self):
        self.parent.set_full_ui()
        self.parent.change_page(PAGE.MENU.value)

    def no_account_label_pressed_event(self, event: QMouseEvent):
        self.parent.change_page(PAGE.SIGN_UP.value)
"""

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
            self.master.full_ui()