import tkinter as tk
from tkinter import (ttk, HORIZONTAL, LEFT, TOP, BOTTOM, X, NW)


class FilterMenu(tk.Toplevel):
    def __init__(self, parent, csv_columns):
        super().__init__(parent)
        self.geometry("400x400")
        self.minsize(300, 300)
        self.csv_columns = csv_columns
        self.create_widgets()

    def create_widgets(self):
        filter_button = ttk.Button(self, text="Filter")

        for col in self.csv_columns:
            min_max_frame = ttk.Frame(self)

            min_label_frame = ttk.Frame(min_max_frame)
            min_label = ttk.Label(min_label_frame, text="Min: " + col)
            min_slider = ttk.Scale(min_label_frame, from_=0, to=100, orient=HORIZONTAL)
            min_label.pack(side=TOP, anchor=NW, fill=X)
            min_slider.pack(side=BOTTOM, padx=20, fill=X, expand=True)
            min_label_frame.pack(side=LEFT, fill=X, expand=True)

            max_label_frame = ttk.Frame(min_max_frame)
            max_label = ttk.Label(max_label_frame, text="Max: " + col)
            max_slider = ttk.Scale(max_label_frame, from_=0, to=100, orient=HORIZONTAL)
            max_label.pack(side=TOP, anchor=NW, fill=X)
            max_slider.pack(side=BOTTOM, padx=20, fill=X, expand=True)
            max_label_frame.pack(side=LEFT, fill=X, expand=True)

            min_max_frame.pack(side=TOP, fill=X, padx=20, pady=5)

        filter_button.pack(side=BOTTOM, fill=X, padx=20, pady=5)
