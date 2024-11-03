from datetime import date
# This class represents an order made by the customer
class Order:
    def __init__(self, cart, customer):
        # Store the cart and customer details in the order
        self.__cart=cart
        self.__customer=customer
        self.__order_date=date.today()
        self.__total_price=self.calculate_total()

    # Method to calculate the total price including discounts and VAT
    def calculate_total(self):
        subtotal=self.__cart.total_price()
        discount=0
        loyalty_discount=0.10 if self.__customer.is_loyalty_member() else 0
        bulk_discount=0.20 if sum(self.__cart.get_cart_items().values())>=5 else 0
        discount=subtotal*(loyalty_discount + bulk_discount)
        vat=(subtotal - discount)*0.08
        total_with_vat=subtotal - discount+vat
        return round(total_with_vat, 2)

    def generate_invoice(self):
        print("Invoice:")
        print("Order Date:", self.__order_date)
        self.__cart.display_cart()

        subtotal=self.__cart.total_price()
        loyalty_discount=0.10 if self.__customer.is_loyalty_member() else 0
        bulk_discount=0.20 if sum(self.__cart.get_cart_items().values())>=5 else 0
        discount=subtotal * (loyalty_discount+bulk_discount)
        vat=(subtotal - discount)*0.08
        total_with_vat=subtotal - discount+vat

        print(f"Subtotal: {subtotal:.2f} AED")
        if loyalty_discount>0:
            print(f"Loyalty Discount (10%): -{subtotal*0.10:.2f} AED")
        if bulk_discount>0:
            print(f"Bulk Purchase Discount (20%): -{subtotal*0.20:.2f} AED")
        print(f"VAT (8%): +{vat:.2f} AED")
        print(f"Total (with VAT): {total_with_vat:.2f} AED")

    # Method to represent the order as a string
    def __str__(self):
        return f"Order for {self.__customer.get_name()} on {self.__order_date}"