import tkinter as tk
from tkinter import ttk, BOTH, X, TOP, filedialog, HORIZONTAL
import tkinter.messagebox as tkm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


# inherits from csv viewer
class AnalyseFile(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.create_widgets()

    def create_widgets(self):
        title_label = ttk.Label(self, text="Upload patient csv to train machine learning algorithm")
        progress_bar = ttk.Progressbar(self, orient=HORIZONTAL)
        upload_button = ttk.Button(self, text="CLick here to upload file",
                                   command=lambda: self.do_machine_learning(progress_bar))

        title_label.pack(side=TOP)
        upload_button.pack(side=TOP, pady=20, fill=X)

    def do_machine_learning(self, progress_bar):
        progress_bar.pack(fill=BOTH)
        csv_data = self.open_csv_ml()
        progress_bar.step(10)
        X = csv_data.drop(['referral'], axis=1)
        y = csv_data['referral']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
        progress_bar.step(10)
        model = RandomForestClassifier(max_depth=7)
        model.fit(X_train, y_train)
        progress_bar.step(79.9)
        tkm.showinfo("Complete!", "Machine learning completed!")

    def open_csv_ml(self):
        file_path = filedialog.askopenfilename(title="Upload CSV File", filetypes=[("CSV files", "*.csv")])
        csv_data = pd.read_csv(file_path)
        csv_data.drop(['encounterId'], inplace=True)
        # removing null values
        csv_data.dropna(inplace=True)
        return csv_data
