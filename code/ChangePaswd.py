import tkinter as tk
from tkinter import ttk
from main import set_password, title_font as font


class ChangePswd(tk.Frame):
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
        display["pswd"] = ttk.Label(frame, text="Enter Password:", font=font)
        display["pswdInput"] = ttk.Entry(frame, textvariable=input, font=font)
        display["submitButton"] = ttk.Button(frame, text="Submit", command=lambda: self.begin_set_pswd(input))

        for i in display.values():
            i.pack(fill='both', expand=True, pady=10, padx=10)

        return frame

    def begin_set_pswd(self, input):
        if input is not None:
            input = input.get()
            set_password(self.user, input)
        else:
            print("Enter password first")
        self.callback()
        self.master.destroy()
