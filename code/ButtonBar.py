import tkinter.ttk as ttk
from tkinter import LEFT
from FilterWindow import FilterWindow


class ButtonBar(ttk.Frame):
    def __init__(self, container, csv_data, toggle, get_hidden):
        super().__init__(container)
        self.toggle = toggle
        self.get_hidden = get_hidden
        # treeview passed from the csv viewer
        self.csv_data = csv_data
        self.filter_button = ttk.Button(self, text="Filter", command=self.open_filter_menu)
        self.filter_button.pack(side=LEFT)

    def reset_button(self):
        self.filter_button.state(["!disabled"])

    # disable the filter button when it is clicked
    def open_filter_menu(self):
        self.filter_button.state(["disabled"])
        FilterWindow(self, self.csv_data, self.toggle, self.get_hidden, self.reset_button)
