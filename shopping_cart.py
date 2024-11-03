# This class represents the shopping cart, where customers add and manage e-books
class ShoppingCart:
    def __init__(self):
      # Dictionary to store e-books and their quantities
        self.__cart={}

# Method to add an e-book to the cart
    def add_to_cart(self, ebook, quantity=1):
        if ebook in self.__cart:
            self.__cart[ebook]+=quantity
        else:
            self.__cart[ebook]=quantity
# Method to remove an e-book from the cart by title
    def remove_from_cart(self, title):
        for ebook in list(self.__cart):
            if ebook.get_title().lower()==title.lower():
                del self.__cart[ebook]
                print(f"'{title}' has been removed from your cart.")
                return
        print(f"'{title}' is not in your cart.")
# Method to update the quantity of an e-book in the cart
    def update_quantity(self, title, quantity):
        for ebook in self.__cart:
            if ebook.get_title().lower()==title.lower():
                if quantity<=0:
                    del self.__cart[ebook]
                    print(f"'{title}' has been removed from your cart.")
                else:
                    self.__cart[ebook]=quantity
                return
        print(f"'{title}' is not in your cart.")

# Method to get all items in the cart
    def get_cart_items(self):
        return self.__cart
# Method to calculate the total price of items in the cart
    def total_price(self):
        return sum(ebook.get_price()*quantity for ebook, quantity in self.__cart.items())
# Method to display all items in the cart
    def display_cart(self):
        print("Your Cart:")
        for ebook, quantity in self.__cart.items():
            print(f"{ebook} | Quantity: {quantity}")
# Method to represent the cart as a string
    def __str__(self):
        return f"ShoppingCart with {len(self.__cart)} items"