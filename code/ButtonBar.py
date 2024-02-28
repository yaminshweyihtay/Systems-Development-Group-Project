import tkinter.ttk as ttk
from tkinter import LEFT


class ButtonBar(ttk.Frame):
    def __init__(self, container, callback):
        super().__init__(container)
        self.callback = callback
        filter_button = ttk.Button(self, text="Filter")
        filter_button.pack(side=LEFT)
