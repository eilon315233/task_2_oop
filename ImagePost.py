from Post import Post


class ImagePost(Post):

    def __init__(self, user, content):
        super().__init__(user, content)

    def display(self):
        print("Shows picture")

    def __str__(self):
        return "{0} posted a picture\n".format(self.get_publisher().get_name())
