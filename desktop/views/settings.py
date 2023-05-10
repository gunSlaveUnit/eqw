from tkinter import Frame, Label, Menu, Entry, Button

import requests

from desktop.logic.create_pdf import create_pdf
from desktop.logic.send_mess import send_email


class Settings(Frame):
    def __init__(self, master=None):
        super(Settings, self).__init__(master)
        master = master

        def send():
            reply = self.master.master.authorized_session.get('http://127.0.0.1:23432/check/last/')
            check = reply.json()
            print(check)
            check_res = check['result']

            to_addr = self.master.master.current_user["email"]
            body_text = check_res
            send_email(to_addr, body_text)

        def printing():
            reply = self.master.master.authorized_session.get('http://127.0.0.1:23432/check/checks/')
            if reply.ok:
                checks = reply.json()
                print(checks)
                first_column= [check['created_at'] for check in checks]
                second_column= [check['result'] for check in checks]

            create_pdf(first_column, second_column)

        self.send_label = Label(self, text="При необходимости Вы можете отправить результаты последней проверки на указанный адрес электронной почты", font=('Helvetica', 12), pady=15, wraplength=400)
        self.send_label.grid(row=0, column=0)

        self.send_button = Button(self, text="Отправить", command=send)
        self.send_button.grid(row=0, column=1)

        self.print_label = Label(self,
                                text="Также Вы имеете возможность распечатать весь свой список проверок",
                                font=('Helvetica', 12), pady=15, wraplength=400)
        self.print_label.grid(row=1, column=0)

        self.print_button = Button(self, text="Распечатать", command=printing)
        self.print_button.grid(row=1, column=1)






