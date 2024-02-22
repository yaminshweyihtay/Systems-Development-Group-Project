import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, HORIZONTAL, NO, X, VERTICAL, RIGHT, LEFT, BOTH, TOP, BOTTOM, NW
import tkinter.messagebox as tkm


class ButtonBar(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        filter_button = ttk.Button(self, text="Filter")
        filter_button.pack(side=LEFT)
        sort_button = ttk.Button(self, text="Sort")
        sort_button.pack(side=LEFT, padx = 15)
