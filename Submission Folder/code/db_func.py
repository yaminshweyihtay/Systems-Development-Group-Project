import tkinter.messagebox as tkm
import mysql.connector
from mysql.connector import errorcode

DATABASE_NAME = "feedingdashboard"
HOST_ADDRESS = "localhost"
USERNAME = "root"
# change this to your root password for your DBMS (MySql)
PASSWD = "root"

CONNECTION_ERROR_MSG = "Unable to connect to the database; please check credentials!"
CONNECTION_ERROR_TITLE = "Connection error!"


# connecting to the database
def connect_to_database():
    try:
        conn = mysql.connector.connect(host=HOST_ADDRESS,
                                       user=USERNAME,
                                       password=PASSWD,
                                       database=DATABASE_NAME)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            tkm.showerror(CONNECTION_ERROR_TITLE, "Invalid DBMS credentials")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            tkm.showerror(CONNECTION_ERROR_TITLE, CONNECTION_ERROR_MSG)
        else:
            tkm.showerror(CONNECTION_ERROR_TITLE, err)
        quit(1)
    else:
        if conn is None:
            tkm.showerror(CONNECTION_ERROR_TITLE, CONNECTION_ERROR_MSG)
        else:
            return conn


# select function used to operate the select sql query
def select(table_name, operator="*", where=None):
    conn = connect_to_database()
    try:
        dbcursor = conn.cursor()
    except mysql.connector.Error:
        tkm.showerror(
            CONNECTION_ERROR_TITLE, CONNECTION_ERROR_MSG
        )
    else:
        if where is None:
            statement = "SELECT {} FROM {};".format(operator, table_name)
        else:
            # formatting function parameters into sql query
            statement = "SELECT {} FROM {} WHERE {};".format(operator, table_name, where)
        dbcursor.execute(statement)
        result = dbcursor.fetchall()
        return result


# select count

def select_count(table_name, operator="*", where=None):
    conn = connect_to_database()
    try:
        dbcursor = conn.cursor()
    except mysql.connector.Error:
        tkm.showerror(
            CONNECTION_ERROR_TITLE, CONNECTION_ERROR_MSG
        )
    else:
        if where is None:
            statement = "SELECT COUNT(*) {} FROM {};".format(operator, table_name)
        else:
            # formatting function parameters into sql query
            statement = "SELECT COUNT(*) FROM {} WHERE {};".format(table_name, where)
        dbcursor.execute(statement)
        result = dbcursor.fetchall()
        return result


def update(table_name, set, where):
    conn = connect_to_database()
    # Checking to see if the connection was successful and if not output an error message
    try:
        dbcursor = conn.cursor()
    except mysql.connector.Error as e:
        tkm.showerror(CONNECTION_ERROR_TITLE, f" {CONNECTION_ERROR_MSG}, {e}")
        return False
    else:
        statement = f"UPDATE {table_name} SET {set} WHERE {where};"
        try:
            dbcursor.execute(statement)
            conn.commit()
        except mysql.connector.Error as e:
            tkm.showerror("Error", f"Error inserting record; {e}")
        finally:
            dbcursor.close()
            conn.close()


def insert(table_name, columns, values):
    conn = connect_to_database()
    # Checking to see if the connection was successful and if not output an error message
    try:
        dbcursor = conn.cursor()
    except mysql.connector.Error as e:
        tkm.showerror(CONNECTION_ERROR_TITLE, f" {CONNECTION_ERROR_MSG} {e}")
        return False
    else:
        placeholders = ', '.join(['%s'] * len(values))
        statement = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
        try:
            dbcursor.execute(statement, values)
            conn.commit()
        except Exception as e:
            tkm.showerror("Error", f"Error inserting record; {e}")
        finally:
            dbcursor.close()
            conn.close()


# Example usage


# select function used to operate the delete sql query
def delete(table_name, where):
    conn = connect_to_database()
    # checking to see if the connection was successful and if not output an error message
    try:
        dbcursor = conn.cursor()
    except mysql.connector.Error:
        tkm.showerror(
            CONNECTION_ERROR_TITLE, CONNECTION_ERROR_MSG
        )
    if not dbcursor:
        return False
    # formatting function parameters into sql query
    statement = "DELETE FROM {} WHERE {}".format(table_name, where)
    dbcursor.execute(statement)
    conn.commit()
    result = dbcursor.fetchall()
    return result
