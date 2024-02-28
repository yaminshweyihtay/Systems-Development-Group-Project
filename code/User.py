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
