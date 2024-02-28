import tkinter as tk
from tkinter import ttk, LEFT, Y, X


class Sidebar(tk.Frame):
    def __init__(self, container, content, display_callback):
        super().__init__(container)
        self.content = content
        self.button_colour = "Coloured.TButton"
        # callback to display contents function in the main gui
        self.display_callback = display_callback
        self.config(bg='gray')
        self.pack(side=LEFT, fill=Y)
        self.button_style = ttk.Style()
        self.button_style.configure("Coloured.TButton", background="gray", padding=(10))
        self.create_widgets()
        
    def create_widgets(self):
        self.upload_csv_button = ttk.Button(self, text="Upload Patient CSV File", style=self.button_colour,
                                            command=lambda: self.display_callback(self.content[0]))
        self.analyse_csv_button = ttk.Button(self, text="Analyse Patient CSV File", style=self.button_colour)
        self.about_button = ttk.Button(self, text="About", style=self.button_colour)
        self.upload_csv_button.pack(pady=15, fill=X)
        self.analyse_csv_button.pack(pady=15, fill=X)
        self.about_button.pack(pady=15, fill=X)
