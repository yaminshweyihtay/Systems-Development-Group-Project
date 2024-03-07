from tkinter import ttk
from customtkinter import CTkScrollableFrame


class CheckPatient(CTkScrollableFrame):
    def __init__(self, container):
        super().__init__(container)
        self.columns = ["encounter_id", "end_tidal_co2", "feed_vol", "feed_vol_adm", "fio2", "fio2_ratio",
                        "insp_time",
                        "oxygen_flow_rate", "peep", "pip", "resp_rate", "sip", "tidal_vol",
                        "tidal_vol_actual", "tidal_vol_kg", "tidal_vol_spon",
                        "bmi"]

        self.configure(corner_radius=0, fg_color="#F1F0F1")

        self.create_widgets()

    def create_widgets(self):
        labels = []
        text_inputs = []
        for column in self.columns:
            label = ttk.Label(self, text=column + ":")
            text_input = ttk.Entry(self)
            labels.append(label)
            text_inputs.append(text_input)
            label.pack(pady=10, fill="both")
            text_input.pack(pady=10, fill="both")

        check_button = ttk.Button(self, text="Check Patient", command=self.check_patient)
        check_button.pack(pady=20)

    def check_patient(self):
        pass
