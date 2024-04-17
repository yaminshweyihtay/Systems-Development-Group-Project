import tkinter as tk
from tkinter import ttk, LEFT, Y, X
from about_page import AboutPage
import os


class Sidebar(tk.Frame):
    def __init__(self, container, display_callback):
        super().__init__(container)
        self.button_colour = "Coloured.TButton"
        # callback to display contents function in the main gui
        self.display_callback = display_callback
        self.config(bg='gray')
        self.pack(side=LEFT, fill=Y)
        self.button_style = ttk.Style()
        self.button_style.configure("Coloured.TButton", background="gray", padding=10)
        self.about_button = ttk.Button(self, text="About", style=self.button_colour,
                                       command=self.open_about_page)
        self.create_widgets()

    def create_widgets(self):
        upload_csv_button = ttk.Button(self, text="Upload Patient CSV File", style=self.button_colour,
                                       command=lambda: self.display_callback(0))
        analyse_csv_button = ttk.Button(self, text="Analyse Patient CSV File", style=self.button_colour,
                                        command=lambda: self.display_callback(1))
        check_patient_button = ttk.Button(self, text="Check Patient", style=self.button_colour,
                                          command=lambda: self.display_callback(2))
        accounts_button = ttk.Button(self, text="Accounts", style=self.button_colour,
                                     command=lambda: self.display_callback(3))
        reports_button = ttk.Button(self, text="Reports",style=self.button_colour,command=self.run_reports)

        upload_csv_button.pack(pady=15, fill=X)
        analyse_csv_button.pack(pady=15, fill=X)
        check_patient_button.pack(pady=15, fill=X)
        accounts_button.pack(pady=15, fill=X)
        self.about_button.pack(pady=15, fill=X)
        reports_button.pack(pady=15,fill=X)

    def open_about_page(self):
        self.about_button.state(["disabled"])
        AboutPage(self, self.reset_about_button)

    def reset_about_button(self):
        self.about_button.state(["!disabled"])

    def run_reports(self):
        os.system("reports.py")
