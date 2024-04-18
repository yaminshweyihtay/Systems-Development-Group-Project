import platform
import tkinter as tk
from tkinter import ttk
from tkinter import BOTH
import ctypes
from customtkinter import CTkScrollableFrame
from main import ICON_PATH, APP_ID

if platform.system() == 'Windows':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)


class AboutPage(tk.Toplevel):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.iconbitmap(ICON_PATH)
        self.title("About")
        self.callback = callback
        self.geometry("760x300")
        self.display_frame = CTkScrollableFrame(self)
        self.display_frame.configure(corner_radius=0, fg_color="#F1F0F1")
        self.minsize(760, 300)
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        # Create and place GUI components
        label_title = ttk.Label(self.display_frame, text="Feeding Dashboard", font=("Arial", 18, "bold"))
        label_title.pack(pady=10)

        label_version = ttk.Label(self.display_frame, text="Version: 1.0", font=("Arial", 12))
        label_version.pack()

        label_overview = ttk.Label(self.display_frame, text="Overview:", font=("Arial", 14, "bold"))
        label_overview.pack(pady=5, anchor="w")

        text_overview = tk.Text(self.display_frame, wrap="word", height=8)
        text_overview.insert(tk.END, """
        The Feeding Dashboard is a sophisticated software application meticulously crafted to meet the intricate needs 
        of Critical Care Unit (CCU) professionals. Engineered with cutting-edge technology and user-centric design 
        principles, it serves as an indispensable tool for optimizing patient care and resource allocation within 
        the CCU.
        """)
        text_overview.config(state="disabled", font=("Arial", 12))
        text_overview.pack(fill="both", expand=True, padx=10)

        label_features = ttk.Label(self.display_frame, text="Features:", font=("Arial", 14, "bold"))
        label_features.pack(pady=5, anchor="w")

        text_features = tk.Text(self.display_frame, wrap="word", height=8)
        text_features.insert(tk.END, """
        • Comprehensive Patient Management
        • Data-driven Decision Support
        • Seamless Data Integration
        • Interactive Data Visualization
        • Robust Reporting Capabilities
        • Cross-Platform Compatibility
        """)
        text_features.config(state="disabled", font=("Arial", 12))
        text_features.pack(fill="both", expand=True, padx=10)

        label_description = ttk.Label(self.display_frame, text="Description of CSV File:",
                                      font=("Arial", 14, "bold"))
        label_description.pack(pady=5, anchor="w")

        text_description = tk.Text(self.display_frame, wrap="word", height=4)
        text_description.insert(tk.END, """
        The CSV file serves as a repository of critical patient data, encompassing a wide range of physiological 
        measurements essential for assessing patient health and determining the need for dietary intervention. 
        """)
        text_description.config(state="disabled", font=("Arial", 12))
        text_description.pack(fill="both", expand=True, padx=10)

        label_requirements = ttk.Label(self.display_frame, text="Requirements:", font=("Arial", 14, "bold"))
        label_requirements.pack(pady=5, anchor="w")

        text_requirements = tk.Text(self.display_frame, wrap="word", height=4)
        text_requirements.insert(tk.END, """
        • Python 3.x
        • Tkinter for GUI
        • MySQL Database
        """)
        text_requirements.config(state="disabled", font=("Arial", 12))
        text_requirements.pack(fill="both", expand=True, padx=10)

        label_developed_by = ttk.Label(self.display_frame, text="Developed by: William, Lewis, Yesen, Yeyi, Yamin",
                                       font=("Arial", 12))
        label_developed_by.pack(pady=10)

        button_close = ttk.Button(self.display_frame, text="Close", command=self.close_window)
        button_close.pack(pady=10)

        self.display_frame.pack(fill=BOTH, expand=True)

    def close_window(self):
        self.callback()
        self.destroy()
