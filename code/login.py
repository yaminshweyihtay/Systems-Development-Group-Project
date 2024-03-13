import tkinter as tk
from tkinter import ttk
from tkinter import LEFT, RIGHT, BOTTOM, X
from main import login, fetch_user_list, title_font


# defining the login gui class
class LoginGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # setting the window size
        self.title("Login")
        self.geometry("400x250")
        self.minsize(180, 180)
        # defining the text input variables
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.bind('<Return>', self.begin_login)
        # placing the widgets on the GUI
        self.create_widgets()

    def create_widgets(self):
        username_frame = ttk.Frame(self)
        password_frame = ttk.Frame(self)
        username_label = ttk.Label(username_frame, text="Username:", font=title_font)
        username_input = ttk.Entry(username_frame, textvariable=self.username, font=title_font)
        password_label = ttk.Label(password_frame, text="Password:", font=title_font)
        password_input = ttk.Entry(password_frame, textvariable=self.password, show="*", font=title_font)
        login_button = ttk.Button(self, text="Submit",
                                  command=self.begin_login)
        username_label.pack(side=LEFT)
        username_input.pack(side=RIGHT, expand=True, fill=X)
        password_label.pack(side=LEFT)
        password_input.pack(side=RIGHT, expand=True, fill=X)
        username_frame.pack(fill=X, padx=5, pady=5, expand=True)
        password_frame.pack(fill=X, padx=5, pady=5, expand=True)
        login_button.pack(side=BOTTOM, fill=X, expand=True)

    def begin_login(self, event=None):
        # variable to make sonar lint happy
        _ = event
        login(self.username.get(), self.password.get(), self)


fetch_user_list()
app = LoginGUI()
app.mainloop()
