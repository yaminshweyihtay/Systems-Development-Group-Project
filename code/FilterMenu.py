import tkinter as tk
from tkinter import (ttk, HORIZONTAL, LEFT, TOP, BOTTOM, X, NW)
from main import find_value_range


class FilterMenu(tk.Toplevel):
    def __init__(self, parent, csv_data):
        super().__init__(parent)
        self.geometry("400x400")
        self.minsize(300, 300)
        self.csv_data = csv_data
        self.create_widgets()

    def create_widgets(self):
        filter_button = ttk.Button(self, text="Filter")
        self.create_filter_widgets()
        filter_button.pack(side=BOTTOM, fill=X, padx=20, pady=5)

    def create_filter_widgets(self):
        columns = self.csv_data['columns']
        for column in columns[1:len(columns) - 1]:
            column_number = columns.index(column)
            min_max_frame = ttk.Frame(self)
            self.create_slider_frame(min_max_frame, column, column_number, "Min")
            self.create_slider_frame(min_max_frame, column, column_number, "Max")
            min_max_frame.pack(side=TOP, fill=X, padx=20, pady=5)

    def create_slider_frame(self, parent, column, column_number, label_text):
        label_frame = ttk.Frame(parent)
        label = ttk.Label(label_frame, text=f"{label_text}: {column}")
        # finding the min and max values for a specific row in the csv
        values = find_value_range(self.csv_data, column_number)
        slider = ttk.Scale(label_frame, from_=values[0], to=values[1], orient=HORIZONTAL)
        if label_text == "Min":
            slider.set(values[0])
        else:
            slider.set(values[1])

        value_label = ttk.Label(label_frame, text=str(slider.get()))

        def update_value_label(value):
            value_label.config(text=str(value))

        slider.config(command=update_value_label)
        label.pack(side=TOP, anchor=NW, fill=X)
        slider.pack(side=TOP, padx=20, fill=X, expand=True)
        value_label.pack(side=TOP, padx=20, fill=X, expand=True)
        label_frame.pack(side=LEFT, fill=X, expand=True)
