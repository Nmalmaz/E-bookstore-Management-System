# The Payment class processes payments based on the payment method chosen.
class Payment:
    def __init__(self, order, payment_method):
        # Store the order and payment method.
        self.__order=order
        self.__payment_method=payment_method

    # Method to process payment.
    def process_payment(self):
        """Processes the payment based on the method selected."""
        if self.__payment_method.lower()=="credit card":
            # Collect card details for credit card payment.
            card_number=input("Enter your credit card number: ")
            expiry_date=input("Enter the expiry date (MM/YY): ")
            ccv=input("Enter the CCV: ")
            # Payment processing logic for credit card
            print(
                f"Processing payment of {self.__order.calculate_total()} AED with Credit Card ending in {card_number[-4:]}.")
        else:
            # Payment processing logic for other methods
            print(f"Processing payment of {self.__order.calculate_total()} AED using {self.__payment_method}.")

        print("Payment successful!")

    # Method to get a string representation of the payment.
    def __str__(self):
        return f"Payment of {self.__order.calculate_total()} AED via {self.__payment_method}"