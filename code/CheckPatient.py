import tkinter as tk
from tkinter import ttk, X, Y, LEFT, RIGHT, BOTH, VERTICAL, NW


class CheckPatient(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columns = ["encounter_id", "end_tidal_co2", "feed_vol", "feed_vol_adm", "fio2", "fio2_ratio",
                        "insp_time",
                        "oxygen_flow_rate", "peep", "pip", "resp_rate", "sip", "tidal_vol",
                        "tidal_vol_actual", "tidal_vol_kg", "tidal_vol_spon",
                        "bmi"]

        self.create_widgets()

    def create_widgets(self):
        check_patient_frame = tk.Frame(self)
        check_patient_frame.pack(fill=BOTH, expand=True)
        canvas = tk.Canvas(check_patient_frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar = ttk.Scrollbar(check_patient_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor=NW)
        text_inputs = []
        for column in self.columns:
            label = ttk.Label(inner_frame, text=column + ":")
            label.pack(pady=10, fill=X)

            text_input = ttk.Entry(inner_frame)
            text_input.pack(pady=10, fill=X, expand=True)
            text_inputs.append(text_input)

        check_button = ttk.Button(inner_frame, text="Check Patient", command=self.check_patient)
        check_button.pack(pady=20, fill=BOTH, expand=True)

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        inner_frame.bind("<Configure>", on_frame_configure)

    def check_patient(self):
        pass
