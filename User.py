from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import SalePost


class User:

    def __init__(self, name, password, is_in):
        self.__name = name
        self.__password = password
        self.__followers = set()
        self.__is_log_in = is_in
        self.__post_num = 0
        self.__notifications = []

    def get_is_log_in(self):
        return self.__is_log_in

    def __add_follower(self, user):
        self.__followers.add(user)

    def __get_followers(self):
        return self.__followers

    def add_notifications(self, text):
        self.__notifications.append(text)

    def follow(self, user):
        if (self.__is_log_in):
            initial_length = len(user.__get_followers())
            user.__add_follower(self)
            if len(user.__get_followers()) > initial_length:
                print(self.get_name() + " started following " + user.get_name())

    def get_last_not(self):
        return self.__notifications[-1]

    def unfollow(self, user):
        if (self.__is_log_in):
            initial_length = len(user.__get_followers())
            user.__followers.remove(self)
            if len(user.__get_followers()) < initial_length:
                print(self.get_name() + " unfollowed " + user.get_name())

    def user_log_in(self):
        self.__is_log_in = True
        print(self.__name + " connected")

    def user_log_out(self):
        self.__is_log_in = False
        print(self.__name + " disconnected")

    def get_name(self):
        return self.__name

    def check_pass(self, password):
        return self.__password == password

    def publish_post(self, typ, content, price=None, location=None):
        if typ == "Text":
            p = TextPost(self, content)
        elif typ == "Image":
            p = ImagePost(self, content)
        elif typ == "Sale":
            p = SalePost(self, content, price, location)
        else:
            return None
        self.__post_num += 1

        for user in self.__followers:
            user.add_notifications(self.get_name() + " has a new post")

        print(p)
        return p

    def print_notifications(self):
        print(self.get_name() + "'s notifications:")
        for notification in self.__notifications:
            print(notification)

    def __str__(self):
        return "User name: {0}, Number of posts: {1}, Number of followers: {2}".format(self.get_name(), self.__post_num, len(self.__followers))

    def __eq__(self, other) -> bool:
        if isinstance(other, User):
            return self.__name == other.get_name()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__name)
