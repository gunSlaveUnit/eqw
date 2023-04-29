from tkinter import Frame, Label, Menu, ttk
from tkinter.messagebox import showinfo
import tkinter as tk

import requests


class AttackInfo(Frame):
    def __init__(self, master=None):
        super(AttackInfo, self).__init__(master)
        master = master

        self.type_label = Label(self, text=" ", font=('Helvetica', 18, "bold"), pady=10)
        self.type_label.grid(row=0, column=2)

        self.info_label = Label(self, text=" ", font=('Helvetica', 8), wraplength=600)
        self.info_label.grid(row=1, column=2, sticky='w')

        reply = requests.get('http://127.0.0.1:23432/attack/')
        attacks = reply.json()
        print(attacks)
        attack_titles = [attack['type'] for attack in attacks]
        attack_info = [attack['info'] for attack in attacks]

        var = tk.Variable(value=attack_titles)

        listbox = tk.Listbox(
            self,
            listvariable=var,
            height=len(attack_titles))

        listbox.grid(row=0, column=0, rowspan=2, sticky="ns")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        scrollbar = ttk.Scrollbar(
            self,
            orient=tk.VERTICAL,
            command=listbox.yview
        )

        listbox['yscrollcommand'] = scrollbar.set

        scrollbar.grid(row=0, rowspan=2, column=1, sticky="ns")

        def items_selected(event):
            # get selected indices
            self.info_label.destroy()
            self.type_label.destroy()
            selected_indices = listbox.curselection()[0]
            print(selected_indices)


            self.type_label = Label(self, text=attack_titles[selected_indices], font=('Helvetica', 18, "bold"), pady=10)
            self.type_label.grid(row=0, column=2, sticky="n")

            self.info_label = Label(self, text=attack_info[selected_indices], font=('Helvetica', 8), wraplength=600)
            self.info_label.grid(row=1, column=2, sticky='n')


        listbox.bind('<<ListboxSelect>>', items_selected)
