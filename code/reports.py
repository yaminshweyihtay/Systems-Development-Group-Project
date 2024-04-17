import ctypes
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from main import validate_pandas_csv, TITLE_FONT, APP_ID, ICON_PATH
from tkinter import ttk, filedialog, TOP, messagebox as tkm, X

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)


class Report(tk.Toplevel):
    def __init__(self, container, callback):
        super().__init__(container)
        self.iconbitmap(ICON_PATH)
        self.geometry("300x120")
        self.resizable(0, 0)
        self.callback = callback
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(self, text="Please select csv location", font=TITLE_FONT)
        open_button = ttk.Button(self, text="Open CSV File", command=self.open_csv)
        title.pack(side=TOP)
        open_button.pack(side=TOP, pady=20, fill=X)

    def close_window(self):
        self.callback()
        self.destroy()

    def open_csv(self):
        file_path = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.destroy()
            self.process_csv(file_path)

    def process_csv(self, file_path):
        input_csv = pd.read_csv(file_path)

        valid = validate_pandas_csv(input_csv)

        if valid:
            number_of_rows = len(input_csv)

            needs_referral = sum(input_csv['referral'] == 1)

            missing_values = input_csv.isna().sum()

            avg_values = input_csv.mean(numeric_only=True)

            my_labels = ["Needs referral: {}".format(needs_referral),
                         "Doesn't need referral: {}".format(number_of_rows - needs_referral)]
            my_labels2 = list(input_csv.columns)

            plt.figure(figsize=(15, 6))
            plt.pie([number_of_rows, needs_referral], labels=my_labels, autopct='%1.1f%%')
            plt.title("Number of patients: {}".format(number_of_rows))
            plt.show()

            plt.figure(figsize=(15, 6))
            plt.bar(my_labels2, missing_values)
            plt.xlabel("Columns")
            plt.ylabel("Number of missing values")
            plt.title("Number of missing values")
            plt.xticks(rotation=90)
            plt.subplots_adjust(bottom=0.3)
            plt.show()

            plt.figure(figsize=(15, 6))
            plt.bar(my_labels2, avg_values)
            plt.xlabel("Columns")
            plt.ylabel("Average values")
            plt.title("Average values")
            plt.xticks(rotation=90)
            plt.subplots_adjust(bottom=0.3)
            plt.show()
            self.callback()
            return True

        if valid is None:
            tkm.showerror("CSV Format Error!", "The CSV is not formatted correctly!")
            return None
        tkm.showerror("CSV Data Error!",
                      "The data in the CSV is invalid, all values should be numerical or empty!")
