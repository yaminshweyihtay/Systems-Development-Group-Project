import tkinter.ttk as ttk
from tkinter import LEFT
from FilterMenu import FilterMenu


class ButtonBar(ttk.Frame):
    def __init__(self, container, csv_data):
        super().__init__(container)
        self.csv_data = csv_data
        filter_button = ttk.Button(self, text="Filter", command=self.open_filter_menu)
        filter_button.pack(side=LEFT)

    def open_filter_menu(self):
        FilterMenu(self, self.csv_data)
