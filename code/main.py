import tkinter.messagebox as tkm
from Patient import Patient
from dbFunc import insert, select
import csv
import os
import bcrypt
from User import User

user_list = []


# reads csv and appends the patient object list, reads in user info
def initialise_objects(file_path, init_user=False):
    global user_list
    # clearing the user list, so it can be updated using fetch_user_list()
    user_list.clear()
    patients = fetch_patients(file_path)
    if init_user:
        user_list = fetch_user_list()
    return patients


def fetch_patients(file_path):
    patients = []
    if file_path:
        try:
            with open(file_path, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                for row in csv_reader:
                    # checking if csv file is too long
                    if len(row) > 18:
                        raise IndexError
                    # append encounterId, end tidal co2, feed vol, feed vol adm, fio2, fio2_ratio, Insp_time
                    # oxygen_flow_rate, peep, pip, resp rate, sip, tidal vol, tidal vol actual, tidal vol kg
                    # tidal vol spon and bmi to patient object
                    patients.append(
                        Patient(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                                row[11], row[12], row[13], row[14], row[15], row[16], row[17])
                    )
        # Index error indicates problem with inputted csv
        except Exception as e:
            if isinstance(e, IndexError):
                tkm.showerror("Error!", "The inputted csv is of the incorrect format!")
            else:
                tkm.showerror("File not found", "The file at ", file_path, " was not found!")
            return False
        return patients


def fetch_user_list():
    users = select('users')
    # append user_id, user_name, password, salt to the user object
    for user in users:
        user_list.append(User(user[0], user[1], user[2], user[3]))
    return user_list


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
            open_main_menu(app)
            return True
        else:
            tkm.showerror("Failure", "Password incorrect!")
            return False


def logout(app):
    app.master.destroy()


def create_user(user_to_add, pswd):
    salt = bcrypt.gensalt()
    pswd = pswd.encode('utf-8')
    pswd = bcrypt.hashpw(pswd, salt)
    salt = str(salt)
    pswd = str(pswd)
    num_of_users = 0
    for user in user_list:
        num_of_users += 1
    user_id = num_of_users + 1
    new_user = User(user_id, user_to_add, pswd, salt)
    user_list.append(new_user)
    try:
        insert("users", ["username, pswd, salt"],
               [user_to_add, pswd, salt])
    except Exception as e:
        tkm.showerror("Failed to add user!", "The user was not added! " + str(e))
    else:
        tkm.showinfo("Add successful!", "The user was added successfully!")


def open_main_menu(app):
    initialise_objects(None)
    app.destroy()
    os.system('python MainGui.py')

