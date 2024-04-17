In order to run our systems development project:

Firstly, please make sure that the libraries: bcrypt, mysql-connector-python, customtkinter,
scikit-learn, pandas, numpy, matplotlib
to do this run "pip list" in the command prompt.
Here are the commands to install the required libraries if the libraries are not installed:
"pip install bcrypt"
"pip install mysql-connector-python"
"pip install customtkinter"
"pip install scikit-learn"
"pip install pandas"
"pip install numpy"
"pip install matplotlib"


Secondly make sure that there are no schemas currently running on my SQL server with the name "feedingdashboard"
and import the MySQL dump which is loacated in /Database"
Then using vs code, edit \code\db_func.py and change "PASSWD" to your root password for your MYSQL server.

Finally go to /code

And double click login.py

The login screen should open (if py files are set to open in python):


The login crededentials are:

Username: "user1234"
Password: "1234"

Source Code is at \code
Database dump is at \Database

