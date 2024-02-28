import tkinter as tk
from tkinter import ttk
from tkinter import LEFT, RIGHT, BOTTOM, X
from main import login

# Setting the default font
font = ("Arial", 14)


# defining the login gui class
class LoginGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # setting the window size
        self.title("Login")
        self.geometry("400x250")
        self.minsize(180, 180)
        # placing the widgets on the GUI
        self.create_widgets()

    def create_widgets(self):
        # defining the text input variables
        username = tk.StringVar()
        password = tk.StringVar()
        username_frame = ttk.Frame(self)
        password_frame = ttk.Frame(self)
        username_label = ttk.Label(username_frame, text="Username:", font=font)
        username_input = ttk.Entry(username_frame, textvariable=username, font=font)
        password_label = ttk.Label(password_frame, text="Password:", font=font)
        password_input = ttk.Entry(password_frame, textvariable=password, show="*", font=font)
        login_button = ttk.Button(self, text="Submit", command=lambda: login(username.get(), password.get(), app))
        username_label.pack(side=LEFT)
        username_input.pack(side=RIGHT, expand=True, fill=X)
        password_label.pack(side=LEFT)
        password_input.pack(side=RIGHT, expand=True, fill=X)
        username_frame.pack(fill=X, padx=5, pady=5, expand=True)
        password_frame.pack(fill=X, padx=5, pady=5, expand=True)
        login_button.pack(side=BOTTOM, fill=X, expand=True)


app = LoginGUI()
app.mainloop()
