"""from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QLineEdit, QLabel

from desktop.config.config import PAGE


class SignUpPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        # Widgets
        self.email = QLineEdit()
        self.password = QLineEdit()
        self.repeat_password = QLineEdit()
        self.sign_up_button = QPushButton()
        self.already_have_account_label = QLabel()

        self.layout = QGridLayout()

        self.set_ui()

    def set_ui(self):
        self.password.setEchoMode(QLineEdit.Password)
        self.repeat_password.setEchoMode(QLineEdit.Password)

        self.sign_up_button.setText("SIGN_UP_BUTTON_TEXT")
        self.sign_up_button.clicked.connect(self.sign_up)



        self.layout.addWidget(self.email)
        self.layout.addWidget(self.password)
        self.layout.addWidget(self.repeat_password)
        self.layout.addWidget(self.sign_up_button)
        self.layout.addWidget(self.already_have_account_label)

        self.setLayout(self.layout)

    def sign_up(self):
        self.parent.set_full_ui()
        self.parent.change_page(PAGE.INFO.value)

    def already_have_account_label_pressed_event(self, event: QMouseEvent):
        self.parent.change_page(PAGE.SIGN_IN.value)
"""

from tkinter import Frame, Label, Entry
from tkinter.ttk import Button
import requests


class Registration(Frame):
    def __init__(self, master=None):
        super(Registration, self).__init__(master)
        master=master

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

