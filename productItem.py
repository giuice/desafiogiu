class ProductItem:

    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
