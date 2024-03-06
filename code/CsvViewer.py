import csv
from ButtonBar import ButtonBar
import tkinter as tk
from tkinter import ttk, filedialog, HORIZONTAL, NO, X, VERTICAL, RIGHT, BOTH, TOP, BOTTOM, NW
import tkinter.messagebox as tkm

from main import initialise_objects


class CsvViewer(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.file_path = None
        self.patients = []
        self.csv_parameters = []
        self.hidden_columns = []
        self.csv_viewer = ttk.Treeview(self, selectmode="browse", show="headings")
        self.create_widgets()

    def create_widgets(self):
        # code for horizontal scroll bar
        x_scroll_bar = ttk.Scrollbar(self, orient=HORIZONTAL)
        x_scroll_bar.configure(command=self.csv_viewer.xview)
        self.csv_viewer.configure(xscrollcommand=x_scroll_bar.set)

        # code for vertical scroll bar
        y_scroll_bar = ttk.Scrollbar(self, orient=VERTICAL, command=self.csv_viewer.yview)
        self.csv_viewer.configure(yscrollcommand=y_scroll_bar.set)
        y_scroll_bar.pack(side=RIGHT, fill=BOTH)
        self.csv_viewer.pack(padx=40, expand=True, fill=BOTH)
        x_scroll_bar.pack(fill=X)

        status_label = tk.Label(self, text="", padx=20, pady=10)
        status_label.pack()

        open_button = ttk.Button(self, text="Open CSV File",
                                 command=lambda: self.open_csv_file(self.csv_viewer, status_label))
        open_button.pack(padx=20, pady=10, side=BOTTOM)

    def open_csv_file(self, csv_viewer, status_label):
        self.file_path = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])
        if self.file_path:
            self.patients = initialise_objects(self.file_path)
            # stop if incorrect csv format
            if not self.patients:
                return False
            self.display_csv_data(csv_viewer, status_label)

    def display_csv_data(self, csv_viewer, status_label):
        try:
            with open(self.file_path, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)  # Read the header row
                csv_viewer.delete(*csv_viewer.get_children())  # Clear the current data
                csv_viewer["columns"] = header
                # read through every column fetch the column names to display
                for col in header:
                    csv_viewer.heading(col, text=col, command=lambda c=col: self.sort_tree_view(csv_viewer, c, True))
                    self.csv_parameters.append(col)
                    csv_viewer.column(col, width=100, stretch=NO)
                # display information from objects
                for patient in self.patients:
                    csv_viewer.insert("", "end", text=patient.get_encounter_id(), values=(patient.get_encounter_id()
                                                                                          , patient.get_end_tidal_co2(),
                                                                                          patient.get_feed_volume(),
                                                                                          patient.get_feed_volume_adm(),
                                                                                          patient.get_fio2(),
                                                                                          patient.get_fio2_ratio(),
                                                                                          patient.get_insp_time(),
                                                                                          patient.get_oxygen_flow_rate(),
                                                                                          patient.get_peep(),
                                                                                          patient.get_pip(),
                                                                                          patient.get_resp_rate(),
                                                                                          patient.get_sip(),
                                                                                          patient.get_tidal_volume(),
                                                                                          patient.get_tidal_volume_actual(),
                                                                                          patient.get_tidal_volume_kg(),
                                                                                          patient.get_tidal_volume_spon(),
                                                                                          patient.get_bmi(),
                                                                                          patient.get_referral()))

                # code for the filter button
                button_bar = ButtonBar(self, csv_viewer, self.toggle_column, self.get_hidden_columns)
                button_bar.pack(padx=40, pady=15, side=TOP, anchor=NW)
                status_label.config(text=f"CSV file loaded: {self.file_path}")
        except Exception as e:
            tkm.showerror("Error", str(e))

    def sort_tree_view(self, tree_view, column, reverse):
        # fetch only rows that are not empty
        non_empty_rows = [k for k in tree_view.get_children('') if tree_view.set(k, column)]
        value_key_pairs = [(tree_view.set(k, column), k) for k in non_empty_rows]
        value_key_pairs.sort(key=lambda t: float(t[0]), reverse=reverse)
        for index, (val, k) in enumerate(value_key_pairs):
            tree_view.move(k, '', index)

        tree_view.heading(column, command=lambda: self.sort_tree_view(tree_view, column, not reverse))

    def toggle_column(self, column_to_toggle):
        # check if column is already hidden
        if not (self.check_if_hidden(column_to_toggle)):
            for item in self.csv_viewer.get_children():
                self.csv_viewer.item(item,
                                     values=[value for i, value in enumerate(self.csv_viewer.item(item)['values']) if
                                             i != column_to_toggle])
            # remove the column
            self.csv_viewer.heading(column_to_toggle, text='')
            self.csv_viewer.column(column_to_toggle, width=0, stretch=NO)
            # add to hidden columns, so it can be unhidden in the future
            self.hidden_columns.append(column_to_toggle)
        else:
            # if column is hidden show it again
            self.csv_viewer.heading(column_to_toggle, text=column_to_toggle)
            self.csv_viewer.column(column_to_toggle, width=100, stretch=NO)
            self.hidden_columns.remove(column_to_toggle)

    def get_hidden_columns(self):
        return self.hidden_columns

    def check_if_hidden(self, column):
        for col in self.get_hidden_columns():
            if col == column:
                return True
        return False

    def get_csv_parameters(self):
        return self.csv_parameters
