from tkinter import Frame, Label, Menu, ttk, NW, X
from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter import ttk
from tkinter import *

import requests

from desktop.logic.data_val import DateChecker


class Info(Frame):
    def __init__(self, master=None):
        super(Info, self).__init__(master)
        master = master

        help = Frame(self)
        self.check_titles = []
        self.check_results = []
        self.check_type = []

        self.encode_type=["Проверка на опасность", "Проверка с определением типов"]

        def handler():
            selection = help.combobox.get()
            print(selection)
            help.label["text"] = f"вы выбрали: {selection}"
            tp = help.combobox.current()
            print(help.combobox.current())
            check_date=DateChecker()
            st = check_date.check_date(help.date_start.get())
            end = check_date.check_date(help.date_end.get())
            print(st)
            if st == None:
                st = 0
            if end == None:
                end = 100000000000000000000000000000000000000
            if tp == None:
                tp = 2

            print(end)
            reply = self.master.master.authorized_session.get(
                f'http://127.0.0.1:23432/check/check/?start_time={st}&end_time={end}&search_type={tp}')
            if reply.ok:
                print("Повезло")
                checks = reply.json()
                #print(checks)
                self.check_titles = [check['created_at'] for check in checks]
                self.check_results = [check['result'] for check in checks]
                self.check_type = [check['check_type'] for check in checks]
                help.listbox.delete(0, 'end')
                for item in self.check_titles:
                    help.listbox.insert('end', item)

        def selected(event):
            handler()

        def end_start():
            handler()

        def end_end():
            handler()

        attack_titles = ["Безопасный трафик", "Опасный трафик   ", "Оба варианта"]

        help.start_label = Label(help, text="Начало:", font=('Helvetica', 12))
        help.start_label.grid(row=0, column=0, pady=10)

        help.date_start = Entry(help, validate="focusout", validatecommand=end_start)
        help.date_start.grid(row=0, column=1)

        help.end_label = Label(help, text="Конец:", font=('Helvetica', 12))
        help.end_label.grid(row=0, column=2)

        help.date_end = Entry(help, validate="focusout", validatecommand=end_end)
        help.date_end.grid(row=0, column=3)

        help.label = ttk.Label(help)
        help.label.grid(row=1, column=0, sticky=NW + E + W, padx=5, pady=5)

        help.combobox = ttk.Combobox(help, values=attack_titles, state="readonly")
        help.combobox.grid(row=2, column=0, sticky=NW + E + W + NS, columnspan=4)
        help.combobox.bind("<<ComboboxSelected>>", selected)

        help.info_label = ttk.Label(help)
        help.info_label.grid(row=3, column=3, sticky=NW + E + W + NS, padx=5, pady=5)

        help.type_label = ttk.Label(help, text='Вид проверки:')
        help.type_label.grid(row=5, column=0,  columnspan=2)

        help.type1_label = ttk.Label(help, wraplength=450, justify=LEFT)
        help.type1_label.grid(row=5, column=2, columnspan=2)

        help.res_label = ttk.Label(help, text='Результат проверки:')
        help.res_label.grid(row=6, column=0,  columnspan=2)

        help.res1_label = ttk.Label(help, wraplength=450, justify=LEFT)
        help.res1_label.grid(row=6, column=2, columnspan=2)

        checks = []

        reply = self.master.master.authorized_session.get('http://127.0.0.1:23432/check/checks/')
        if reply.ok:
            checks = reply.json()
            print(checks)
            self.check_titles = [check['created_at'] for check in checks]
            check_help = [check['id'] for check in checks]
        var = tk.Variable(value=self.check_titles)

        help.listbox = tk.Listbox(
            help,
            listvariable=var,
            height=len(attack_titles))

        help.listbox.grid(row=3, column=0, rowspan=2, columnspan=4, sticky=EW + NS)

        scrollbar = ttk.Scrollbar(
            help,
            orient=tk.VERTICAL,
            command=help.listbox.yview
        )

        help.listbox['yscrollcommand'] = scrollbar.set

        scrollbar.grid(row=3, rowspan=2, column=5, sticky=W + NS)

        def items_selected(event):
            # get selected indices
            selected_indices = help.listbox.curselection()[0]
            print(selected_indices)
            help.type1_label['text'] = self.encode_type[self.check_type[selected_indices]]
            help.res1_label['text'] = self.check_results[selected_indices]

        help.listbox.bind('<<ListboxSelect>>', items_selected)

        help.pack(anchor="nw")
