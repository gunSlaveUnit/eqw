from tkinter import Frame, Label, Menu, ttk, NW, X
from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter import ttk
from tkinter import *

import requests


class Info(Frame):
    def __init__(self, master=None):
        super(Info, self).__init__(master)
        master = master

        help=Frame(self)

        def selected(event):
            # получаем выделенный элемент
            selection = help.combobox.get()
            print(selection)
            help.label["text"] = f"вы выбрали: {selection}"

        reply = requests.get('http://127.0.0.1:23432/attack/')
        attacks = reply.json()
        #print(attacks)
        attack_titles = [attack['type'] for attack in attacks]

        help.start_label = Label(help, text="Начало:", font=('Helvetica', 12))
        help.start_label.grid(row=0, column=0, pady=10 )


        help.date_start = Entry(help)
        help.date_start.grid(row=0, column=1)

        help.end_label = Label(help, text="Конец:", font=('Helvetica', 12))
        help.end_label.grid(row=0, column=2)

        help.date_end = Entry(help)
        help.date_end.grid(row=0, column=3)


        help.label = ttk.Label(help)
        help.label.grid(row=1, column=0, sticky=NW+E+W, padx=5, pady=5)

        help.combobox = ttk.Combobox(help, values=attack_titles, state="readonly")
        help.combobox.grid(row=2, column=0, sticky=NW+E+W, columnspan=4)
        help.combobox.bind("<<ComboboxSelected>>", selected)

        help.info_label = ttk.Label(help)
        help.info_label.grid(row=3, column=3, sticky=NW + E + W, padx=5, pady=5)

        checks=[]
        check_titles=[]
        reply = master.master.authorized_session.get('http://127.0.0.1:23432/check/checks/')
        if reply.ok:
            checks = reply.json()
            print(checks)
            check_titles = [check['created_at'] for check in checks]
            check_info = [check['id'] for check in checks]


        var = tk.Variable(value=check_titles)

        listbox = tk.Listbox(
            help,
            listvariable=var,
            height=len(attack_titles))

        listbox.grid(row=3, column=0, rowspan=2, sticky="e")

        #help.rowconfigure(0, weight=1)
        #help.rowconfigure(1, weight=1)
        scrollbar = ttk.Scrollbar(
            help,
            orient=tk.VERTICAL,
            command=listbox.yview
        )

        listbox['yscrollcommand'] = scrollbar.set

        scrollbar.grid(row=3, rowspan=2, column=1, sticky=W+NS)

        def items_selected(event):
            # get selected indices
            selected_indices = listbox.curselection()[0]
            print(selected_indices)

        listbox.bind('<<ListboxSelect>>', items_selected)



        help.pack(anchor="nw")