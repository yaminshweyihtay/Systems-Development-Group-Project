import tkinter.messagebox as tkm
from Patient import Patient
import csv


# reads csv and appends the patient object list
def initialise_objects(file_path):
    patients = []
    try:
        with open(file_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                # append encounterId, end tidal co2, feed vol, feed vol adm, fio2, fio2_ratio, Insp_time
                # oxygen_flow_rate, peep, pip, resp rate, sip, tidal vol, tidal vol actual, tidal vol kg
                # tidal vol spon and bmi to patient object
                try:
                    patients.append(
                        Patient(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                                row[11], row[12], row[13], row[14], row[15], row[16], row[17])
                    )
                # check if csv is the correct format
                except IndexError:
                    tkm.showerror("Invalid CSV", "The uploaded csv is not the correct format!")
                    return False
    except FileNotFoundError:
        tkm.showerror("File not found", "The file at ", file_path, " was not found!")
        return False
    return patients
