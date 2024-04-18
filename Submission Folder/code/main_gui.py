import os
import platform
import tkinter as tk
from tkinter import LEFT, Y, BOTH
import ctypes
from sidebar import Sidebar
from csv_viewer import CsvViewer
from analyse_file import AnalyseFile
from check_patient import CheckPatient
from user_management import UserManagement
from main import load_current_user, ICON_PATH, APP_ID

if platform.system() == 'Windows':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)


class MainGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(ICON_PATH)
        self.logged_in = load_current_user()
        if not self.is_logged_in():
            exit(1)

        self.protocol("WM_DELETE_WINDOW", self.close_gui)
        self.geometry("800x600")
        self.title("Critical Care Unit Management Program")
        self.minsize(400, 400)
        # array of frames which can be displayed as content
        self.content = []
        self.content.append(CsvViewer(self))
        self.content.append(AnalyseFile(self))
        self.content.append(CheckPatient(self))
        self.content.append(UserManagement(self))
        # sending frames to sidebar
        self.side_bar = Sidebar(self, self.display_content)
        self.side_bar.pack(side=LEFT, fill=Y)
        # binding to adjust width of the sidebar if width of window is changed
        self.bind("<Configure>", lambda event: self.get_width())

    def get_width(self):
        # set the new sidebar width to 25% of the window width
        side_bar_width = self.winfo_width() * 0.25
        self.side_bar.config(width=side_bar_width)

    def display_content(self, index):
        # Hide the previous frame
        if hasattr(self, "current_frame"):
            self.current_frame.pack_forget()

        # Raise the new frame
        frame = self.content[index]
        frame.pack(fill=BOTH, expand=True)
        frame.tkraise()

        # Set the current_frame attribute to the newly displayed frame
        self.current_frame = frame

    # function for removing the current user and machine learning file when app closed
    def close_gui(self):
        self.destroy()
        if os.path.exists("currentUser.pkl"):
            os.remove("currentUser.pkl")

        if os.path.exists("ccu_machine_learning_model.pkl"):
            os.remove("ccu_machine_learning_model.pkl")

    def is_logged_in(self):
        return self.logged_in


app = MainGui()
app.mainloop()
