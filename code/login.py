import tkinter as tk
from tkinter import ttk
from main import initialise_objects, login

# Setting the default font
font = ("Arial", 14)


# defining the login gui class
class LoginGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # setting the window size and making the window unable to be resized
        self.title("Login")
        self.geometry("400x250")
        self.resizable(0, 0)
        # placing the widgets on the GUI
        self.create_widgets()
        self.columnconfigure(0, weight=1)

    def create_widgets(self):
        # defining the text input variables
        username = tk.StringVar()
        password = tk.StringVar()
        login_display = {}
        login_display["usernameLabel"] = ttk.Label(text="Username:", font=font)
        login_display["usernameInput"] = ttk.Entry(textvariable=username, font=font)
        login_display["passwordLabel"] = ttk.Label(text="Password:", font=font)
        login_display["passwordInput"] = ttk.Entry(textvariable=password, show="*", font=font)
        login_display["submitButton"] = ttk.Button(text="Submit", command=lambda: login(username.get(), password.get(), app))
        index = 0
        # displaying the widgets
        for display in login_display.values():
            display.grid(row=index, columnspan=2, padx=20, pady=3, sticky="ew")
            index += 1


initialise_objects()
app = LoginGUI()
app.mainloop()
