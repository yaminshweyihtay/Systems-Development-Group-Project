import tkinter as tk
from tkinter import ttk, VERTICAL, HORIZONTAL, LEFT, RIGHT, X, Y, BOTH, NW, ALL
from main import find_value_range


class FilterMenu(tk.Toplevel):
    def __init__(self, parent, csv_data):
        super().__init__(parent)
        self.geometry("400x400")
        self.minsize(300, 300)
        self.csv_data = csv_data
        self.create_widgets()

    @staticmethod
    def update_value_label(value, label):
        label.config(text=value)

    def create_widgets(self):
        filter_frame = tk.Frame(self)
        filter_frame.pack(fill=BOTH, expand=True)

        canvas = tk.Canvas(filter_frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = ttk.Scrollbar(filter_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor=NW)

        # Function to update scroll region
        def update_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox(ALL))

        inner_frame.bind("<Configure>", update_scroll_region)

        # Function to update canvas size
        def update_canvas_size(event):
            canvas.itemconfig(inner_frame_window, width=event.width)

        #  call update canvas size when window resized
        canvas.bind("<Configure>", update_canvas_size)

        inner_frame_window = canvas.create_window((0, 0), window=inner_frame, anchor=NW)

        filter_button = ttk.Button(inner_frame, text="Filter")
        filter_button.pack(side=tk.BOTTOM, fill=X, padx=20, pady=5)

        columns = self.csv_data['columns']
        labels = []
        sliders = []

        # go through all columns while not including the first and last index
        for column in columns[1:-1]:
            column_range = find_value_range(self.csv_data, column)

            min_label = ttk.Label(inner_frame, text="Min: " + column)
            min_label.pack(fill=X)
            min_value_label = ttk.Label(inner_frame, text="")
            min_value_label.pack(fill=X)
            min_slider = ttk.Scale(inner_frame, from_=column_range[0], to=column_range[1], orient=HORIZONTAL)
            min_slider.pack(fill=X)

            max_label = ttk.Label(inner_frame, text="Max: " + column)
            max_label.pack(fill=X)
            max_value_label = ttk.Label(inner_frame, text="")
            max_value_label.pack(fill=X)
            max_slider = ttk.Scale(inner_frame, from_=column_range[0], to=column_range[1], orient=HORIZONTAL)
            max_slider.pack(fill=X)

            min_slider.config(command=lambda value, label=min_value_label: self.update_value_label(value, label))
            max_slider.config(command=lambda value, label=max_value_label: self.update_value_label(value, label))

            # set the default values of the sliders
            min_slider.set(column_range[0])
            max_slider.set(column_range[1])

            labels.extend([min_label, max_label])
            sliders.extend([min_slider, max_slider])
