import tkinter
from tkinter import LEFT, Y
from Sidebar import Sidebar
from CsvViewer import CsvViewer
from main import initialise_objects


class MainGui(tkinter.Tk):
    initialise_objects()
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Critical Care Unit Management Program")
        self.minsize(400, 400)
        self.content = []
        self.content.append(CsvViewer(self))
        self.side_bar = Sidebar(self, self.content)
        self.side_bar.pack(side=LEFT, fill=Y)
        self.bind("<Configure>", lambda event: self.get_width())

    def get_width(self):
        side_bar_width = self.winfo_width() * 0.25
        self.side_bar.config(width=side_bar_width)


app = MainGui()
app.mainloop()

