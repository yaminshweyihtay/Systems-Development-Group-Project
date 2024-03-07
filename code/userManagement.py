import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
from main import *

font = ("Arial", 14)

# creating an order viewer frame
class UserManagement(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.currentUser = load_current_user()
        view = self.create_widgets()
        view.pack()

    def create_widgets(self):
        frame = ttk.Frame(self)
        display = {}
        
        # defining the buttons
        display['chngUsername'] = ttk.Button(frame, text="Change Username", command=lambda: self.open_new_window(ChngUsername,
                                        "Change Username", self.refresh, currentUser))
        display['chngPswd'] = ttk.Button(frame, text="Change Password", command=lambda: self.open_new_window(ChngPswd,
                                        "Change Password", self.refresh, currentUser))
        display['addUser'] = ttk.Button(frame, text="Add User", command=lambda: self.open_new_window(AddUser,
                                        "Add User", self.refresh))

        for i in display.values():
            i.pack(fill='both', expand=True, pady=10, padx=10)

        return frame

    def refresh(self):
        for widget in self.winfo_children():
            widget.destroy()
        view = self.create_widgets()
        view.pack()


    def open_new_window(self, root, title, callback, user = None):
        new_window = tk.Toplevel(self)
        new_window.title(title)
        if user is not None:
            new_frame = root(new_window, callback, user)
        else:
            new_frame = root(new_window, callback)
        new_frame.pack()
        new_window.wait_window()


class ChngUsername(tk.Frame):
    def __init__(self, container, callback, user):
        super().__init__(container)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.callback = callback
        self.user = user
        view = self.create_widgets()
        view.pack()

    def create_widgets(self):
        frame = ttk.Frame(self)

        user0 = ''.join(self.user)
        for i in user_list:
            if i.get_username() == user0:
                user = i

        input = tk.StringVar()
        display = {}
        display["user"] = ttk.Label(frame, text="Enter Username:", font=font)
        display["userinput"] = ttk.Entry(frame, textvariable=input, font=font)
        display["submitButton"] = ttk.Button(frame, text="Submit", command=lambda: self.begin_user_set(user, input))

        for i in display.values():
            i.pack(fill='both', expand=True, pady=10, padx=10)

        return frame
    
    def begin_set_user(self, user, input):
        if input is not None:
            input = input.get()
            #set_username(input, user)
        else:
            print("Enter username first")
        self.callback()
        self.master.destroy()

class ChngPswd(tk.Frame):
    def __init__(self, container, callback, user):
        super().__init__(container)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.callback = callback
        self.user = user
        view = self.create_widgets()
        view.pack()

    def create_widgets(self):
        frame = ttk.Frame(self)

        user0 = ''.join(self.user)
        for i in user_list:
            if i.get_username() == user0:
                user = i

        input = tk.StringVar()
        display = {}
        display["pswd"] = ttk.Label(frame, text="Enter Password:", font=font)
        display["pswdInput"] = ttk.Entry(frame, textvariable=input, font=font)
        display["submitButton"] = ttk.Button(frame, text="Submit", command=lambda: self.begin_set_pswd(user, input))

        for i in display.values():
            i.pack(fill='both', expand=True, pady=10, padx=10)

        return frame
    
    def begin_set_pswd(self, user, input):
        if input is not None:
            input = input.get()
            #set_password(input, user)
        else:
            print("Enter password first")
        self.callback()
        self.master.destroy()


class AddUser(tk.Frame):
    def __init__(self, container, callback):
        super().__init__(container)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.callback = callback
        view = self.create_widgets()
        view.pack()

    def create_widgets(self):
        frame = ttk.Frame(self)
        username = tk.StringVar()
        password = tk.StringVar()

        display = {}
        display["user"] = ttk.Label(frame, text="Enter Username:", font=font)
        display["userinput"] = ttk.Entry(frame, textvariable=username, font=font)
        display["pswd"] = ttk.Label(frame, text="Enter Password:", font=font)
        display["pswdInput"] = ttk.Entry(frame, textvariable=password, font=font)
        display["submitButton"] = ttk.Button(frame, text="Submit", command=lambda: self.begin_add_user(username,
                                                                            password))

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

