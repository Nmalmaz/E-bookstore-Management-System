from datetime import date

# This class represents a single ebook with details like title, author, genre, and price.
class Ebook:
    def __init__(self, title, author, publication_date, genre, price):
        # Private attributes to store ebook details
        self.__title=title
        self.__author=author
        self.__publication_date=publication_date
        self.__genre=genre
        self.__price=price

# Method to get the title of the e-book
    def get_title(self):
        return self.__title
# Method to get the price of the e-book
    def get_price(self):
        return self.__price
# Method to set or change the price of the e-book
    def set_price(self, price):
        """Sets the price of the e-book."""
        self.__price = price
# Method to show the details of the e-book as a string
    def __str__(self):
        return (f"Ebook: {self.__title}, Author: {self.__author}, " f"Publication Date: {self.__publication_date}, Genre: {self.__genre}, Price: {self.__price} AED")