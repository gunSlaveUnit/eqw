
from tkinter import Frame, Label, Menu, ttk
from tkinter.messagebox import showinfo
import tkinter as tk


class Info(Frame):
    def __init__(self, master=None):
        super(Info, self).__init__(master)
        master = master

        langs = ('Java', 'C#', 'C', 'C++', 'Python',
                 'Go', 'JavaScript', 'PHP', 'Swift')

        var = tk.Variable(value=langs)

        listbox = tk.Listbox(
            self,
            listvariable=var,
            height=6,
            selectmode=tk.EXTENDED)

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
        #scrollbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)

        def items_selected(event):
            # get selected indices
            selected_indices = listbox.curselection()
            # get selected items
            selected_langs = ",".join([listbox.get(i) for i in selected_indices])
            msg = f'You selected: {selected_langs}'

            showinfo(title='Information', message=msg)

        listbox.bind('<<ListboxSelect>>', items_selected)


