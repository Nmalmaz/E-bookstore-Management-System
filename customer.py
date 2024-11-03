# This class represents a customer with their details and loyalty status
class Customer:
    def __init__(self, name, contact_info, loyalty_member=False):
      # Private attributes for storing customer details
        self.__name=name
        self.__contact_info=contact_info
        self.__loyalty_member=loyalty_member
# Method to check if the customer is a loyalty member
    def is_loyalty_member(self):
        return self.__loyalty_member
# Method to get the customer's name
    def get_name(self):
        return self.__name
# Method to show the customer's details as a string
    def __str__(self):
        return f"Customer: {self.__name}, Contact Info: {self.__contact_info}, Loyalty Member: {self.__loyalty_member}"