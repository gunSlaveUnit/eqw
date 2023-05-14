from tkinter import Frame, Label, Menu
import tkinter as tk

from desktop.logic.auth import exit_func
from desktop.materials.strings import NAME


class AppMenu(Frame):
    def __init__(self, master=None):
        super(AppMenu, self).__init__(master)


        header_label = Label(self, text=NAME)
        header_label.pack()



