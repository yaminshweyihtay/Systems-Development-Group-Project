import tkinter as tk
from tkinter import LEFT, Y, BOTH
from Sidebar import Sidebar
from CsvViewer import CsvViewer
from AnalyseFile import AnalyseFile
from CheckPatient import CheckPatient
from userManagement import UserManagement


class MainGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Critical Care Unit Management Program")
        self.minsize(400, 400)
        # array of frames which can be displayed as content
        self.content = []
        self.content.append(CsvViewer(self))
        self.content.append(AnalyseFile(self))
        self.content.append(CheckPatient(self))
        self.content.append(UserManagement(self))
        self.current_display = None
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


app = MainGui()
app.mainloop()
