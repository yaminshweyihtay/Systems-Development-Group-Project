import tkinter as tk
from tkinter import ttk, BOTTOM, X


class FilterWindow(tk.Toplevel):
    def __init__(self, parent, csv_data, toggle, get_hidden, reset_button):
        super().__init__(parent)
        self.toggle = toggle
        self.get_hidden = get_hidden
        # code to ensure the filter button will re-enable if the window is closed
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.reset_button = reset_button
        self.title("Show / Hide Columns")
        self.geometry("400x520")
        # treeview passed on from csv_viewer
        self.csv_data = csv_data
        self.create_widgets()

    def create_widgets(self):
        columns = self.csv_data['columns']

        close_button = ttk.Button(self, text="Close", command=self.close_window)

        check_boxes = []

        # display check boxes each labeled using the treeview's column names
        for column in columns[1:-1]:
            state = tk.BooleanVar(value=self.mark_check_boxes(column))
            show_hide_column = ttk.Checkbutton(self, text=column, variable=state,
                                               command=lambda col=column, var=state: self.toggle_column(col))
            show_hide_column.pack(fill=X, pady=5)
            check_boxes.append(show_hide_column)

        close_button.pack(fill=X, side=BOTTOM)

    def toggle_column(self, column):
        self.toggle(column)

    def mark_check_boxes(self, column):
        hidden_columns = self.get_hidden()
        return column not in hidden_columns

    def close_window(self):
        self.destroy()
        # resetting the filter button to enabled
        self.reset_button()
