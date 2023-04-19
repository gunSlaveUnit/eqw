from tkinter import Frame, Label, Entry
from tkinter.ttk import Button


class Registration(Frame):
    def __init__(self, master=None):
        super(Registration, self).__init__(master)

        header_label = Label(self, text="Регистрация")
        header_label.pack()

        email_label = Label(self, text="Электронная почта")
        email_label.pack()

        email_entry = Entry(self)
        email_entry.pack()

        username_label = Label(self, text="Имя пользователя")
        username_label.pack()

        username_entry = Entry(self)
        username_entry.pack()

        password_label = Label(self, text="Пароль")
        password_label.pack()

        password_entry = Entry(self)
        password_entry.pack()

        sign_up_button = Button(self, text="Зарегистрироваться")
        sign_up_button.pack()
