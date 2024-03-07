import tkinter as tk
from tkinter import ttk, messagebox as tkm
from customtkinter import CTkScrollableFrame
from main import load_machine_learning_model
import numpy as np


class CheckPatient(CTkScrollableFrame):
    def __init__(self, container):
        super().__init__(container)
        self.columns = ["end_tidal_co2", "feed_vol", "feed_vol_adm", "fio2", "fio2_ratio",
                        "insp_time",
                        "oxygen_flow_rate", "peep", "pip", "resp_rate", "sip", "tidal_vol",
                        "tidal_vol_actual", "tidal_vol_kg", "tidal_vol_spon",
                        "bmi"]

        self.configure(corner_radius=0, fg_color="#F1F0F1")
        self.labels = []
        self.text_inputs = []
        self.user_inputs = []
        self.create_widgets()

    def create_widgets(self):
        for column in self.columns:
            label = ttk.Label(self, text=column + ":")
            user_in = tk.StringVar()
            text_input = ttk.Entry(self, textvariable=user_in)
            self.user_inputs.append(user_in)
            self.labels.append(label)
            self.text_inputs.append(text_input)
            label.pack(pady=10, fill="both")
            text_input.pack(pady=10, fill="both")

        check_button = ttk.Button(self, text="Check Patient", command=self.check_patient)
        check_button.pack(pady=20)

    def check_patient(self):
        converted_inputs = self.validate_inputs()
        model = load_machine_learning_model()
        if not model:
            tkm.showerror("Analysis needed!",
                          "A machine learning algorithm needs to be trained first, head to analyse patient csv file")
        else:
            print("Here!")
            converted_inputs = converted_inputs.reshape(1, -1)  # Assign the reshaped array back to converted_inputs
            prediction = model.predict(converted_inputs)
            if prediction == 0:
                tkm.showinfo("Dietitian should not be required",
                             "Based on the data inputted, the patient should not need to see a dietitian")
            else:
                tkm.showinfo("Dietitian should be required", "Based on the data inputted, the patient should see a "
                                                             "dietitian")

    def validate_inputs(self):
        converted_inputs = []
        for inputs in self.user_inputs:
            try:
                float_value = float(inputs.get())
                converted_inputs.append(float_value)
            except ValueError:
                tkm.showerror("Invalid input", "The inputted values must be of numerical form!")
                return False
        return np.array(converted_inputs)
