import tkinter.messagebox as tkm
from Patient import Patient
from dbFunc import *
import csv
import pickle
import bcrypt
import os

user_list = []
FILE_NAME = "currentUser.pkl"

class User:
    def __init__(self, username=None, passwd=None, salt=None):
        self.__username = username
        self.__password = passwd
        self.__salt = salt

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_salt(self):
        return self.__salt

    def set_username(self, username):
        self.__username = username

    def set_password(self, new_password):
        self.__password = new_password

    def set_salt(self, salt):
        self.__salt = salt

# reads csv and appends the patient object list
def initialise_objects(file_path=None):
    patients = []
    user_list.clear()
    users = select('users')
    for user in users:
        user_list.append(User(user[1], user[2], user[3]))

    if file_path:
        try:
            with open(file_path, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                for row in csv_reader:
                    # append encounterId, end tidal co2, feed vol, feed vol adm, fio2, fio2_ratio, Insp_time
                    # oxygen_flow_rate, peep, pip, resp rate, sip, tidal vol, tidal vol actual, tidal vol kg
                    # tidal vol spon and bmi to patient object
                    patients.append(
                        Patient(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                                row[11], row[12], row[13], row[14], row[15], row[16], row[17])
                    )
        except FileNotFoundError:
            tkm.showerror("File not found", "The file at ", file_path, " was not found!")
            return False
        return patients



def save_current_user():
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(currentUser, file)

# function for logging in
def login(username=None, password=None, app=None):
    # making sure current user is assigned correctly
    global currentUser
    user_to_login = None
    # and assigning the userToLogin variable to that user object
    for user in user_list:
        if username is not None:
            if user.get_username() == username:
                currentUser = user
                user_to_login = user
                save_current_user()
                break
            else:
                continue
        else:
            continue
    # if no user to login is found then the user does not exist
    if user_to_login is None:
        tkm.showerror("Error", "User not found!")
    else:
        # checking if the password is correct
        password = password.encode('utf-8')
        salt = user_to_login.get_salt()
        salt = salt.encode('utf-8')
        salt = salt[2:len(salt) - 1]
        hashedpw = bcrypt.hashpw(password, salt)
        password_to_check = user_to_login.get_password()
        # converting the password to bytes for hashing
        password_to_check = password_to_check.encode('utf-8')
        password_to_check = password_to_check[2:len(password_to_check) - 1]
        if password_to_check == hashedpw:
            # if password is correct assign the current user to the selected user object
            currentUser = user_to_login
            save_current_user()
            open_main_menu(app)
            return True
        else:
            tkm.showerror("Failure", "Password incorrect!")
            return False
        
def logout(app):
    initialise_objects()
    global currentUser
    app.master.destroy()
    currentUser = None
    os.remove(FILE_NAME)
    os.system('python login.py')
        
def create_user(user, pswd):
    salt = bcrypt.gensalt()
    pswd = pswd.encode('utf-8')
    pswd = bcrypt.hashpw(pswd, salt)
    salt = str(salt)
    pswd = str(pswd)
    new_user = User(user, pswd)
    user_list.append(new_user)
    try:
        insert("users", ["username, pswd, salt"],
               [user, pswd, salt])
    except Exception as e:
        tkm.showerror("Failed to add user!", "The user was not added! " + str(e))
    else:
        tkm.showinfo("Add successful!", "The user was added successfully!")

def open_main_menu(app):
    initialise_objects()
    app.destroy()
    os.system('python MainGui.py')

