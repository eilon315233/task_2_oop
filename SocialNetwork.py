from User import User

def __is_pass_valid__(password):
    if 4 <= len(password) <= 8:
        return True
    return False
class SocialNetwork:

    def __init__(self, name):
        self.__name = name
        self.__users = []
        print("The social network " + name + " was created!")


    def __get_user_by_name__(self, name):
        for user in self.__users:
            if user.get_name() == name:
                return user
        return None
    def sign_up (self, name, password):

        if self.__is_user_exist__(name) or not __is_pass_valid__(password):
            return None

        user = User(name, password, True)
        self.__users.append(user)

        return user

    def log_out(self, name):
        user = self.__get_user_by_name__(name)
        if user is None:
            return
        user.user_log_out()

    def log_in(self, name, password):
        user = self.__get_user_by_name__(name)
        if user is None:
            return None
        if user.check_pass(password):
            user.user_log_in()

    def __is_user_exist__(self, name):
        for user in self.__users:
            if user.get_name() == name:
                return True
        return False

    def __str__(self):
        ans = self.__name + " social network:\n"
        for user in self.__users:
            ans += str(user) + "\n"
        return ans







