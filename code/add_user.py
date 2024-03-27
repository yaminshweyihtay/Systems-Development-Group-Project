import tkinter as tk
from tkinter import ttk
from main import create_user, TITLE_FONT


class AddUser(tk.Frame):
    def __init__(self, container, callback):
        super().__init__(container)
        self.callback = callback
        view = self.create_widgets()
        view.pack()

    def create_widgets(self):
        frame = ttk.Frame(self)
        username = tk.StringVar()
        password = tk.StringVar()

        display = {"user": ttk.Label(frame, text="Enter Username:", font=TITLE_FONT),
                   "userinput": ttk.Entry(frame, textvariable=username, font=TITLE_FONT),
                   "pswd": ttk.Label(frame, text="Enter Password:", font=TITLE_FONT),
                   "pswdInput": ttk.Entry(frame, textvariable=password, font=TITLE_FONT),
                   "submitButton": ttk.Button(frame, text="Submit", command=lambda: self.begin_add_user(username,
                                                                                                        password))}

        for i in display.values():
            i.pack(fill='both', expand=True, pady=10, padx=10)

        return frame

    def begin_add_user(self, user, pswd):
        if user and pswd is not None:
            user = user.get()
            pswd = pswd.get()
            create_user(user, pswd)
        else:
            print("Missing parameters")
        self.callback()
        self.master.destroy()
