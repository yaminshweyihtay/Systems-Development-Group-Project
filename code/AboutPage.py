import tkinter as tk
from tkinter import ttk
from tkinter import VERTICAL, LEFT, RIGHT, Y, BOTH


class AboutPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("About")
        self.geometry("760x300")
        self.maxsize(760, 780)
        self.minsize(760, 300)

        page_frame = ttk.Frame(self)

        page_canvas = tk.Canvas(page_frame)

        page_scroll_bar = ttk.Scrollbar(page_frame, orient=VERTICAL, command=page_canvas.yview)

        scrollable_page_frame = ttk.Frame(page_canvas)

        scrollable_page_frame.bind(
            "<Configure>",
            lambda e: page_canvas.configure(
                scrollregion=page_canvas.bbox("all")
            )
        )

        # Create and place GUI components
        label_title = ttk.Label(scrollable_page_frame, text="Feeding Dashboard", font=("Arial", 18, "bold"))
        label_title.pack(pady=10)

        label_version = ttk.Label(scrollable_page_frame, text="Version: 1.0", font=("Arial", 12))
        label_version.pack()

        label_overview = ttk.Label(scrollable_page_frame, text="Overview:", font=("Arial", 14, "bold"))
        label_overview.pack(pady=5, anchor="w")

        text_overview = tk.Text(scrollable_page_frame, wrap="word", height=8)
        text_overview.insert(tk.END, """
        The Feeding Dashboard is a sophisticated software application meticulously crafted to meet the intricate needs 
        of Critical Care Unit (CCU) professionals. Engineered with cutting-edge technology and user-centric design 
        principles, it serves as an indispensable tool for optimizing patient care and resource allocation within 
        the CCU.
        """)
        text_overview.config(state="disabled", font=("Arial", 12))
        text_overview.pack(fill="both", expand=True, padx=10)

        label_features = ttk.Label(scrollable_page_frame, text="Features:", font=("Arial", 14, "bold"))
        label_features.pack(pady=5, anchor="w")

        text_features = tk.Text(scrollable_page_frame, wrap="word", height=8)
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

        label_description = ttk.Label(scrollable_page_frame, text="Description of CSV File:",
                                      font=("Arial", 14, "bold"))
        label_description.pack(pady=5, anchor="w")

        text_description = tk.Text(scrollable_page_frame, wrap="word", height=4)
        text_description.insert(tk.END, """
        The CSV file serves as a repository of critical patient data, encompassing a wide range of physiological 
        measurements essential for assessing patient health and determining the need for dietary intervention. 
        """)
        text_description.config(state="disabled", font=("Arial", 12))
        text_description.pack(fill="both", expand=True, padx=10)

        label_requirements = ttk.Label(scrollable_page_frame, text="Requirements:", font=("Arial", 14, "bold"))
        label_requirements.pack(pady=5, anchor="w")

        text_requirements = tk.Text(scrollable_page_frame, wrap="word", height=4)
        text_requirements.insert(tk.END, """
        • Python 3.x
        • Tkinter for GUI
        • MySQL Database (Optional)
        """)
        text_requirements.config(state="disabled", font=("Arial", 12))
        text_requirements.pack(fill="both", expand=True, padx=10)

        label_developed_by = ttk.Label(scrollable_page_frame, text="Developed by: William, Lewis, Yesen, Yeyi, Yamin",
                                       font=("Arial", 12))
        label_developed_by.pack(pady=10)

        button_close = ttk.Button(scrollable_page_frame, text="Close", command=self.destroy)
        button_close.pack(pady=10)
        # page_scroll_bar.config(command=page_frame.yview)
        page_canvas.create_window((0, 0), window=scrollable_page_frame, anchor="nw")
        page_canvas.configure(yscrollcommand=page_scroll_bar.set)
        page_frame.pack(fill=BOTH, expand=True)
        page_canvas.pack(side=LEFT, fill=BOTH, expand=True)
        page_scroll_bar.pack(side=RIGHT, fill=Y)
