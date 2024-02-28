import csv
from ButtonBar import ButtonBar
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, HORIZONTAL, NO, X, VERTICAL, RIGHT, BOTH, TOP, BOTTOM, NW
import tkinter.messagebox as tkm

from main import initialise_objects


class CsvViewer(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.file_path = None
        self.patients = []
        button_bar = ButtonBar(self)
        button_bar.pack(padx=40, pady=15, side=TOP, anchor=NW)
        self.create_widgets()

    def create_widgets(self):
        csv_viewer = ttk.Treeview(self, selectmode="browse", show="headings")
        # code for horizontal scroll bar
        x_scroll_bar = ttk.Scrollbar(self, orient=HORIZONTAL)
        x_scroll_bar.configure(command=csv_viewer.xview)
        csv_viewer.configure(xscrollcommand=x_scroll_bar.set)

        # code for vertical scroll bar
        y_scroll_bar = ttk.Scrollbar(self, orient=VERTICAL, command=csv_viewer.yview)
        csv_viewer.configure(yscrollcommand=y_scroll_bar.set)
        y_scroll_bar.pack(side=RIGHT, fill=BOTH)
        csv_viewer.pack(padx=40, expand=True, fill=BOTH)
        x_scroll_bar.pack(fill=X)

        status_label = tk.Label(self, text="", padx=20, pady=10)
        status_label.pack()

        open_button = ttk.Button(self, text="Open CSV File",
                                 command=lambda: self.open_csv_file(csv_viewer, status_label))
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
                for col in header:
                    csv_viewer.heading(col, text=col)
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

                status_label.config(text=f"CSV file loaded: {self.file_path}")

        except Exception as e:
            tkm.showerror("Error", str(e))
