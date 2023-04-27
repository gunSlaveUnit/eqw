import time
from tkinter import Frame, Label, Menu, Button, Scale, IntVar
from tkinter.constants import HORIZONTAL
from tkinter.filedialog import askopenfile
from tkinter.ttk import Progressbar

from desktop.logic.network import network
from desktop.materials.strings import LOAD_LABEL, LOAD_BUTTON, CHECK_BUTTON


class Check(Frame):

    def __init__(self, master=None):
        super(Check, self).__init__(master)
        master = master
        self.path = ''
        self.value=0

        def open_file():
            file_path = askopenfile(mode='r', filetypes=[('Text Files', '*txt')])
            if file_path is not None:
                #print(file_path.name)

                self.path=file_path.name
                #print(path)

        def uploadFiles():
            #print(self.path)
            #print(scale.get())
            self.value=scale.get()
            res=network(self.path, self.value)
            print(res)

            pb1 = Progressbar(
                self,
                orient=HORIZONTAL,
                length=300,
                mode='determinate'
            )
            pb1.grid(row=4, columnspan=3, pady=20)
            for i in range(5):
                self.update_idletasks()
                pb1['value'] += 20
                time.sleep(1)
            pb1.destroy()
            Label(self, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)

        info_label = Label(
            self,
            text='Хотите знать тип атаки?'
        )
        info_label.grid(row=0, column=0,  pady=20, sticky="w", rowspan=2)
        no_label = Label(
            self,
            text='Нет'
        )

        def change_value():
            if self.value==0:
                self.value=1
            else:
                self.value=0


        no_label.grid(row=0, column=1, sticky="w")

        scale = Scale(self, from_=0, to=1, orient="horizontal")

        scale.grid(row=1, column=1, columnspan=2)
        add_label = Label(
            self,
            text=LOAD_LABEL
        )
        yes_label = Label(
            self,
            text='Да'
        )
        yes_label.grid(row=0, column=2, pady=20, sticky="e")

        add_label.grid(row=2, column=0, pady=50, sticky="w")

        add_file_button = Button(
            self,
            text=LOAD_BUTTON,
            command=lambda: open_file()
        )
        add_file_button.grid(row=2, column=3)



        load_button = Button(
            self,
            text=CHECK_BUTTON,
            command=uploadFiles
        )
        load_button.grid(row=3, column=1, columnspan=2, pady=10)



