import tkinter.ttk as ttk
from tkinter import LEFT
from FilterWindow import FilterWindow


class ButtonBar(ttk.Frame):
    def __init__(self, container, csv_data, toggle, get_hidden):
        super().__init__(container)
        self.toggle = toggle
        self.get_hidden = get_hidden
        self.csv_data = csv_data
        filter_button = ttk.Button(self, text="Filter", command=self.open_filter_menu)
        filter_button.pack(side=LEFT)

    def open_filter_menu(self):
        FilterWindow(self, self.csv_data, self.toggle, self.get_hidden)
