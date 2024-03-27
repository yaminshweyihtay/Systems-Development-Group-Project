class User:
    def __init__(self, user_id, username, passwd, salt):
        self.__user_id = user_id
        self.__username = username
        self.__password = passwd
        self.__salt = salt

    # setters
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_username(self, username):
        self.__username = username

    def set_password(self, new_password):
        self.__password = new_password

    def set_salt(self, salt):
        self.__salt = salt

    # getters
    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_salt(self):
        return self.__salt

    def get_user_id(self):
        return self.__user_id
