import tkinter as tk
from tkinter import ttk
from main import set_username, title_font as font


class ChangeUsername(tk.Frame):
    def __init__(self, container, callback, user):
        super().__init__(container)
        self.callback = callback
        self.user = user
        view = self.create_widgets()
        view.pack()

    def create_widgets(self):
        frame = ttk.Frame(self)

        input = tk.StringVar()
        display = {}
        display["user"] = ttk.Label(frame, text="Enter Username:", font=font)
        display["userinput"] = ttk.Entry(frame, textvariable=input, font=font)
        display["submitButton"] = ttk.Button(frame, text="Submit", command=lambda: self.begin_set_user(input))

        for i in display.values():
            i.pack(fill='both', expand=True, pady=10, padx=10)

        return frame

    def begin_set_user(self, input):
        if input is not None:
            input = input.get()
            set_username(self.user, input)
        else:
            print("Enter username first")
        self.callback()
        self.master.destroy()
