import tkinter.ttk as ttk
from tkinter import LEFT


class ButtonBar(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        filter_button = ttk.Button(self, text="Filter")
        filter_button.pack(side=LEFT)
        sort_button = ttk.Button(self, text="Sort")
        sort_button.pack(side=LEFT, padx=15)
