import tkinter as tk
from tkinter import ttk, BOTH, X, TOP, filedialog, HORIZONTAL
import tkinter.messagebox as tkm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from main import export_machine_learning_model, TITLE_FONT, CONTENT_FONT, validate_pandas_csv


class AnalyseFile(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.create_widgets()

    def create_widgets(self):
        title_label = ttk.Label(self, text="Upload patient csv to train machine learning algorithm", font=TITLE_FONT)

        progress_label = ttk.Label(self, text="Machine learning in progress:", font=CONTENT_FONT)

        progress_bar = ttk.Progressbar(self, orient=HORIZONTAL)
        upload_button = ttk.Button(self, text="Click here to upload file",
                                   command=lambda: self.do_machine_learning(progress_bar, progress_label,
                                                                            upload_button))

        title_label.pack(side=TOP)
        upload_button.pack(side=TOP, pady=20, fill=X)

    def do_machine_learning(self, progress_bar, progress_label, upload_button):
        upload_button.state(["disabled"])
        progress_label.pack(fill=BOTH)
        progress_bar.pack(fill=BOTH)
        try:
            csv_data = self.open_csv()
        except ValueError:
            tkm.showerror("CSV Data Error!",
                          "The data in the CSV is invalid, all values should be numerical or empty!")
        except IndexError:
            tkm.showerror("CSV Format Error!", "The CSV is not formatted correctly!")

        except FileNotFoundError:
            pass

        else:
            progress_bar.step(10)
            # setting X and y to map the referral feature
            X = csv_data.drop(['referral'], axis=1)
            y = csv_data['referral']
            # Splitting the dataset into training data
            X_train, _, y_train, _ = train_test_split(X, y, test_size=0.3, random_state=1)
            progress_bar.step(10)
            # Training the machine learning model
            model = RandomForestClassifier(max_depth=7, n_jobs=-1)
            model.fit(X_train, y_train)
            progress_bar.step(79.9)
            export_machine_learning_model(model)
            tkm.showinfo("Complete!", "Machine learning completed!")
            upload_button.state(["!disabled"])
            progress_label.pack_forget()
        finally:
            upload_button.state(["!disabled"])
            progress_label.pack_forget()

    @staticmethod
    def open_csv():
        file_path = filedialog.askopenfilename(title="Upload CSV File", filetypes=[("CSV files", "*.csv")])
        # if statement to prevent error if user chooses not to upload file
        if file_path:
            csv_data = pd.read_csv(file_path)
            valid = validate_pandas_csv(csv_data)
            if valid:
                # having to do this because apparently ['encounterId'] isn't there, but it actually is
                csv_data.drop(columns=[col for col in csv_data.columns if col.lower() == 'encounterid'], inplace=True)
                # removing null values
                csv_data.dropna(inplace=True)
                return csv_data
            else:
                if valid is None:
                    raise IndexError
                raise ValueError
        raise FileNotFoundError
