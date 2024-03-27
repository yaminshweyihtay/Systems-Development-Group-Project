import tkinter as tk
from tkinter import ttk
from main import load_current_user, logout
from change_username import ChangeUsername
from change_passwd import ChangePswd
from add_user import AddUser


class UserManagement(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.currentUser = load_current_user()
        view = self.create_widgets()
        view.pack()

    def create_widgets(self):
        frame = ttk.Frame(self)
        display = {'currentUser': ttk.Label(frame, text="Logged in as %s" % (self.currentUser.get_username())),
                   'chngUsername': ttk.Button(frame, text="Change Username",
                                              command=lambda: self.open_new_window(ChangeUsername,
                                                                                   "Change Username", self.refresh,
                                                                                   self.currentUser)),
                   'chngPswd': ttk.Button(frame, text="Change Password",
                                          command=lambda: self.open_new_window(ChangePswd,
                                                                               "Change "
                                                                               "Password",
                                                                               self.refresh,
                                                                               self.currentUser)),
                   'addUser': ttk.Button(frame, text="Add User", command=lambda: self.open_new_window(AddUser,
                                                                                                      "Add User",
                                                                                                      self.refresh)),
                   'logout': ttk.Button(frame, text="Logout", command=lambda: logout(self))}

        # defining the buttons

        for i in display.values():
            i.pack(fill='both', expand=True, pady=10, padx=10)

        return frame

    def refresh(self):
        for widget in self.winfo_children():
            widget.destroy()
        view = self.create_widgets()
        view.pack()

    def open_new_window(self, root, title, callback, user=None):
        new_window = tk.Toplevel(self)
        new_window.title(title)
        if user is not None:
            new_frame = root(new_window, callback, user)
        else:
            new_frame = root(new_window, callback)
        new_frame.pack()
        new_window.wait_window()
