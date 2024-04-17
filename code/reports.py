import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import Button, filedialog

class Report(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.create_widgets()

    def create_widgets(self):
        self.open_button = Button(self)
        self.open_button["text"] = "Open CSV File"
        self.open_button["command"] = self.open_csv
        self.open_button.pack(side="top")

    def open_csv(self):
        file_path = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.process_csv(file_path)

    def process_csv(self, file_path):
        df = pd.read_csv(file_path)

        number_of_rows = len(df)
        print("Total patients:")
        print(number_of_rows)

        needs_referral = sum(df['referral'] == 1)
        print("Patients in need of referral:")
        print(needs_referral)

        missing_values = df.isna().sum()
        print("Number of missing values for each column:")
        print(missing_values)

        avg_values = df.mean(numeric_only=True)
        print("Average values for each column:")
        print(avg_values)

        my_labels = ["Needs referral: {}".format(needs_referral), "Doesn't need referral: {}".format(number_of_rows - needs_referral)]
        my_labels2 = list(df.columns)
        
        plt.figure(figsize=(15, 6))
        plt.pie([number_of_rows, needs_referral], labels=my_labels, autopct='%1.1f%%')
        plt.title("Number of patients: {}".format(number_of_rows))
        plt.show()

        plt.figure(figsize=(15, 6))
        plt.bar(my_labels2, missing_values)
        plt.xlabel("Columns")
        plt.ylabel("Number of missing values")
        plt.title("Number of missing values")
        plt.show()

        plt.figure(figsize=(15, 6))
        plt.bar(my_labels2, avg_values)
        plt.xlabel("Columns")
        plt.ylabel("Average values")
        plt.title("Average values")
        plt.show()
