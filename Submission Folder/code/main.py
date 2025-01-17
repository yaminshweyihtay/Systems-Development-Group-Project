import tkinter.messagebox as tkm
import csv
import pickle
import os
from io import StringIO
import joblib
import bcrypt
from patient import Patient
from db_func import insert, select, update
from user import User

APP_ID = 'mycompany.myproduct.subproduct.version'
TITLE_FONT = ("Arial", 14)
CONTENT_FONT = ("Arial", 12)
ICON_PATH = "Icon.ico"
# the column names for a valid csv file
COLUMNS = ["encounterId", "end_tidal_co2", "feed_vol", "feed_vol_adm", "fio2", "fio2_ratio", "insp_time",
           "oxygen_flow_rate", "peep", "pip", "resp_rate", "sip", "tidal_vol", "tidal_vol_actual", "tidal_vol_kg",
           "tidal_vol_spon", "bmi", "referral"]
user_list = []
FILE_NAME = "currentUser.pkl"


# reads csv and appends the patient object list, reads in user info
def initialise_objects(file_path, init_user=False):
    global user_list
    # clearing the user list, so it can be updated using fetch_user_list()
    user_list.clear()
    try:
        patients = fetch_patients(file_path)
        # Index error indicates problem with inputted csv
    except TypeError:
        tkm.showerror("Column Error!", "The inputted csv is of the incorrect format!")
        return False

    except ValueError:
        tkm.showerror("Value Error!", "There is invalid data in the CSV! All values in the CSV must be a number "
                                      "or empty space!")
        return False

    except FileNotFoundError:
        tkm.showerror("File not found", "The file at " + str(file_path) + " was not found!")
        return False

    if init_user:
        user_list = fetch_user_list()
    return patients


def fetch_patients(file_path):
    patients = []
    if file_path:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            cols = next(csv_file)
            if cols != COLUMNS:
                raise TypeError

            for row in csv_file:
                # Check if all values in the row are numbers or empty strings
                if all(cell == '' or cell.replace('.', '', 1).isdigit() or (
                        cell.startswith('-') and cell[1:].replace('.', '', 1).isdigit()) for cell in row):
                    # If all values are numbers, append the Patient object
                    patients.append(
                        Patient(row[0], row[1], row[2], row[3], row[4],
                                row[5], row[6], row[7], row[8], row[9],
                                row[10], row[11], row[12], row[13], row[14],
                                row[15], row[16], row[17])
                    )
                else:
                    raise ValueError
    return patients


def validate_pandas_csv(csv_data):
    # if statement to check if CSV is valid
    if list(csv_data.columns) != COLUMNS:
        return None
    csv_string = csv_data.to_csv(index=False)
    csv_file = StringIO(csv_string)
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        if all(cell == '' or cell.replace('.', '', 1).isdigit() or (
                cell.startswith('-') and cell[1:].replace('.', '', 1).isdigit()) for cell in row):
            continue
        return False
    return True


def fetch_user_list():
    users = select('users')
    if users is None:
        return False
    # append user_id, user_name, password, salt to the user object
    for user in users:
        user_list.append(User(user[0], user[1], user[2], user[3]))
    return user_list


def does_user_exist(user_name):
    for user in user_list:
        if user.get_username() == user_name:
            user_to_login = user
            return user_to_login
    return False


# function for logging in
def login(username=None, password=None, app=None):
    # making sure current user is assigned correctly
    global current_user
    user_to_login = does_user_exist(username)
    # if no user to login is found then the user does not exist
    if user_to_login is False:
        tkm.showerror("Error", "User not found!")
        return False

    salt = user_to_login.get_salt()
    password_to_check = user_to_login.get_password()
    if check_password(salt, password, password_to_check):
        # if password is correct assign the current user to the selected user object
        current_user = user_to_login
        save_current_user()
        app.destroy()
        open_main_menu()
        return True
    tkm.showerror("Failure", "Password incorrect!")
    return False


def save_current_user():
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(current_user, file)


def load_current_user():
    try:
        with open(FILE_NAME, 'rb') as file:
            user = pickle.load(file)
            return user
    except FileNotFoundError:
        tkm.showerror("Login Required!", "You need to login first before accessing the main program!")
        return False


def logout(app):
    initialise_objects(None)
    global current_user
    app.master.destroy()
    current_user = None
    os.remove(FILE_NAME)
    os.system('python login.py')


def create_user(user_to_add, pswd):
    salt, pswd = generate_password(pswd)
    user_id = len(user_list) + 1
    new_user = User(user_id, user_to_add, pswd, salt)
    user_list.append(new_user)
    try:
        insert("users", ["username, pswd, salt"],
               [user_to_add, pswd, salt])
    except Exception as e:
        tkm.showerror("Failed to add user!", "The user was not added! " + str(e))
    else:
        tkm.showinfo("Add successful!", "The user was added successfully!")


def set_username(user, new_user_name):
    user.set_username(new_user_name)
    user_id = user.get_user_id()
    user_id = int(user_id)
    try:
        update("users", f"username = '{new_user_name}'", f"userId = {user_id}")
    except Exception as e:
        tkm.showerror("Failed to change username!", "The username was not changed! " + str(e))
    else:
        tkm.showinfo("Change successful!", "The username was changed successfully!")


def generate_password(password):
    salt = bcrypt.gensalt()
    password = password.encode('utf-8')
    password = bcrypt.hashpw(password, salt)
    return str(salt), str(password)


def check_password(salt, input_password, correct_password):
    input_password = input_password.encode('utf-8')
    salt = salt.encode('utf-8')
    salt = salt[2:len(salt) - 1]
    hashed_password = bcrypt.hashpw(input_password, salt)
    # converting the password to bytes for hashing
    if str(hashed_password) == str(correct_password):
        return True
    return False


def set_password(user, newpassword):
    salt, pswd = generate_password(newpassword)
    user.set_password(pswd)
    user.set_salt(salt)
    user_id = user.get_user_id()
    user_id = int(user_id)
    try:
        update("users", f'pswd = "{pswd}", salt = "{salt}"', f"userId = {user_id}")
    except Exception as e:
        tkm.showerror("Failed to change password!", "The password was not changed! " + str(e))
    else:
        tkm.showinfo("Change successful!", "The password was changed successfully!")


def open_main_menu():
    initialise_objects(None)
    os.system('python main_gui.py')


def export_machine_learning_model(model):
    joblib.dump(model, 'ccu_machine_learning_model.pkl')


def load_machine_learning_model():
    try:
        return joblib.load('ccu_machine_learning_model.pkl')
    except FileNotFoundError:
        return False
