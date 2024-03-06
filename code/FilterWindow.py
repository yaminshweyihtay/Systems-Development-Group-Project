import tkinter as tk
from tkinter import ttk, BOTTOM, X


class FilterWindow(tk.Toplevel):
    def __init__(self, parent, csv_data, toggle, get_hidden):
        super().__init__(parent)
        self.toggle = toggle
        self.get_hidden = get_hidden
        self.title("Show / Hide Columns")
        self.geometry("400x520")
        self.csv_data = csv_data
        self.create_widgets()

    def create_widgets(self):
        columns = self.csv_data['columns']

        close_button = ttk.Button(self, text="Close", command=self.destroy)

        check_boxes = []

        for column in columns[1:-1]:
            state = tk.BooleanVar(value=self.mark_check_boxes(column))
            show_hide_column = ttk.Checkbutton(self, text=column, variable=state,
                                               command=lambda col=column, var=state: self.toggle_column(col, var))
            show_hide_column.pack(fill=X, pady=5)
            check_boxes.append(show_hide_column)

        close_button.pack(fill=X, side=BOTTOM)

    def toggle_column(self, column, var):
        self.toggle(column)

    def mark_check_boxes(self, column):
        hidden_columns = self.get_hidden()
        return column not in hidden_columns

