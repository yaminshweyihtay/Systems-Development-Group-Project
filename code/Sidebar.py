import tkinter as tk
from tkinter import ttk, LEFT, Y, X, BOTH


class Sidebar(tk.Frame):
    def __init__(self, container, content):
        super().__init__(container)
        self.content = content
        self.config(bg='gray')
        self.pack(side=LEFT, fill=Y)
        self.button_style = ttk.Style()
        self.button_style.configure("Coloured.TButton", background="gray", padding=(10))
        self.create_widgets()

    def create_widgets(self):
        self.upload_csv_button = ttk.Button(self, text="Upload Patient CSV File", style="Coloured.TButton",
                                            command=lambda: self.display_content(self.content[0]))
        self.analyse_csv_button = ttk.Button(self, text="Analyse Patient CSV File", style="Coloured.TButton")
        self.about_button = ttk.Button(self, text="About", style="Coloured.TButton")
        self.upload_csv_button.pack(pady=15, fill=X)
        self.analyse_csv_button.pack(pady=15, fill=X)
        self.about_button.pack(pady=15, fill=X)

    def display_content(self, content):
        content.pack(fill=BOTH, expand=True)
