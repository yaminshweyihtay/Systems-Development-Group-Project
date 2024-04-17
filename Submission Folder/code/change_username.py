import tkinter as tk
from tkinter import ttk
from main import set_username, TITLE_FONT


class ChangeUsername(tk.Frame):
    def __init__(self, container, callback, user):
        super().__init__(container)
        self.callback = callback
        self.user = user
        view = self.create_widgets()
        view.pack()

    def create_widgets(self):
        frame = ttk.Frame(self)

        new_username_input = tk.StringVar()
        display = {"user": ttk.Label(frame, text="Enter Username:", font=TITLE_FONT),
                   "userinput": ttk.Entry(frame, textvariable=new_username_input, font=TITLE_FONT),
                   "submitButton": ttk.Button(frame, text="Submit",
                                              command=lambda: self.begin_set_user(new_username_input))}

        for i in display.values():
            i.pack(fill='both', expand=True, pady=10, padx=10)

        return frame

    def begin_set_user(self, new_user_name):
        if new_user_name is not None:
            new_user_name = new_user_name.get()
            set_username(self.user, new_user_name)
        else:
            print("Enter username first")
        self.callback()
        self.master.destroy()
