import tkinter as tk
from tkinter import LEFT, Y, BOTH
from Sidebar import Sidebar
from CsvViewer import CsvViewer
from AboutPage import AboutPage #


class MainGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Critical Care Unit Management Program")
        self.minsize(400, 400)
        # array of frames which can be displayed as content
        self.content = []
        self.content.append(CsvViewer(self))
        self.side_bar = Sidebar(self, self.content, self.display_content)
        self.side_bar.pack(side=LEFT, fill=Y)
        # binding to adjust width of the sidebar if width of window is changed
        self.bind("<Configure>", lambda event: self.get_width())

    def get_width(self):
        # set the new sidebar width to 25% of the window width
        side_bar_width = self.winfo_width() * 0.25
        self.side_bar.config(width=side_bar_width)

    @staticmethod
    def display_content(content):
        content.pack(fill=BOTH, expand=True)

    def open_about_page(self): #
        about_window = AboutPage(self)


app = MainGui()
app.mainloop()
