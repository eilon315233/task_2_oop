from Post import Post


class SalePost(Post):

    def __init__(self, user, content, price, location):
        super().__init__(user, content)
        self.__price = price
        self.__location = location
        self.__is_available = True

    def sold(self, password):
        if not self.get_publisher().check_pass(password):
            return
        self.__is_available = False
        print(self.get_publisher().get_name() + "'s product is sold")

    def get_publisher(self):
        return super().get_publisher()

    def __str__(self):
        ans = self.get_publisher().get_name() + " posted a product for sale:\n"
        if self.__is_available:
            ans += "For sale! "
        else:
            ans += "Sold! "
        ans += super().__str__()
        ans += ", price: " + str(self.__price) + ", pickup from: " + self.__location + "\n"
        return ans

    def discount(self, percent, password):
        if not self.get_publisher().check_pass(password):
            return
        d = percent / 100
        d -= 1
        d = abs(d)
        self.__price *= d
        print("Discount on " + self.get_publisher().get_name() + " product! the new price is: " + str(self.__price))



