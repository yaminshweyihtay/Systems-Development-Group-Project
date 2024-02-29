import tkinter as tk
from tkinter import Text, END

class AboutPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("About")
        self.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="Feeding Dashboard", font=("Arial", 18, "bold"))
        title_label.pack(pady=20)

        version_label = tk.Label(self, text="Version: 1.0", font=("Arial", 14))
        version_label.pack()

        overview_label = tk.Label(self, text="Overview:", font=("Arial", 14, "underline"))
        overview_label.pack(anchor="w", pady=10)

        overview_text = Text(self, wrap="word", height=6, width=60)
        overview_text.insert(END, "The Feeding Dashboard is a sophisticated software application meticulously crafted to meet the intricate needs of Critical Care Unit (CCU) professionals. Engineered with cutting-edge technology and user-centric design principles, it serves as an indispensable tool for optimizing patient care and resource allocation within the CCU.")
        overview_text.config(state="disabled")
        overview_text.pack()

        features_label = tk.Label(self, text="Features:", font=("Arial", 14, "underline"))
        features_label.pack(anchor="w", pady=10)

        features_text = Text(self, wrap="word", height=10, width=60)
        features_text.insert(END, "Comprehensive Patient Management: Seamlessly view and manage a comprehensive list of patients admitted to the CCU, with intuitive filtering and flagging functionalities to identify patients in need of dietary intervention.\n\nData-driven Decision Support: Leverage the power of data analytics and machine learning algorithms to analyze physiological measurements and provide actionable insights, facilitating informed decision-making in patient care.\n\nSeamless Data Integration: Effortlessly upload patient data from CSV files, ensuring seamless integration with existing hospital information systems and minimizing manual data entry errors.\n\nInteractive Data Visualization: Gain deeper insights into individual patient data through interactive visualization tools, including customizable graphs and charts that highlight key trends and patterns.\n\nRobust Reporting Capabilities: Generate detailed reports summarizing patient information, complete with comprehensive tables and visual representations, empowering healthcare professionals with actionable intelligence.\n\nCross-Platform Compatibility: Built with cross-platform compatibility in mind, the Feeding Dashboard is fully compatible with Windows, Mac, and Linux operating systems, providing flexibility and accessibility across diverse environments.")
        features_text.config(state="disabled")
        features_text.pack()

        description_label = tk.Label(self, text="Description of CSV File:", font=("Arial", 14, "underline"))
        description_label.pack(anchor="w", pady=10)

        description_text = Text(self, wrap="word", height=6, width=60)
        description_text.insert(END, "The CSV file serves as a repository of critical patient data, encompassing a wide range of physiological measurements essential for assessing patient health and determining the need for dietary intervention. Each row in the CSV file represents a unique patient, with fields meticulously organized to capture vital information such as end-tidal CO2, feed volume, FIO2, and referral status.")
        description_text.config(state="disabled")
        description_text.pack()

        requirements_label = tk.Label(self, text="Requirements:", font=("Arial", 14, "underline"))
        requirements_label.pack(anchor="w", pady=10)

        requirements_text = Text(self, wrap="word", height=6, width=60)
        requirements_text.insert(END, "Python 3.x: Leveraging the latest advancements in Python programming, the Feeding Dashboard delivers robust performance and flexibility.\n\nTkinter for GUI: Utilizing the Tkinter library, the Feeding Dashboard offers a seamless and intuitive graphical user interface (GUI), ensuring a smooth user experience for healthcare professionals.\n\nMySQL Database (Optional): For organizations seeking enhanced data management capabilities, integration with a MySQL database provides secure and scalable storage solutions.")
        requirements_text.config(state="disabled")
        requirements_text.pack()

        developed_by_label = tk.Label(self, text="Developed by: William, Lewis, Yesen, Yeyi, Yamin", font=("Arial", 14))
        developed_by_label.pack(anchor="w", pady=10)

        contact_label = tk.Label(self, text="For support or inquiries, please contact abc@gmail.com", font=("Arial", 14))
        contact_label.pack(anchor="w", pady=10)

        close_button = tk.Button(self, text="Close", command=self.destroy)
        close_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide main window
    about_page = AboutPage(root)
    root.mainloop()
