from ebook import Ebook
from catalog import Catalog
from customer import Customer
from shopping_cart import ShoppingCart
from order import Order
from payment import Payment
# Main function to run the e-book store application.
def main():
  # Create a catalog and add e-books to it.
    catalog = Catalog()
    catalog.add_ebook(Ebook("From Rags to Riches: A Story of Abu Dhabi", "Mohammed Al Fahim", "June 9, 1995", "History, Nonfiction, Biography", 300))
    catalog.add_ebook(Ebook("Sheikh Zayed: An Eternal Legacy", "Myrna Ayad", "November 2021", "Art, Biography, History", 1000))
    catalog.add_ebook(Ebook("Qessati", "Sheikh Mohammed bin Rashid Al Maktoum", "January 1", "Autobiography", 400))
    catalog.add_ebook(Ebook("Camels Love Dubai", "Stephen Wilkins", "January 1, 2009", "Fiction", 150))
    catalog.add_ebook(Ebook("Arabian Sands", "Sir Wilfred Thesiger", "1959", "Travel, History, Adventure", 200))

    print("Welcome to the Great E-book Store!")
    name=input("Enter your name: ")
    contact_info=input("Enter your contact information (phone number or email): ")
    is_loyalty=input("Are you a loyalty member? (yes/no): ").strip().lower()=="yes"

# Create a Customer object with the provided details.
    customer=Customer(name, contact_info, is_loyalty)
    cart=ShoppingCart() # Initialize an empty shopping cart.

    while True:
      # Display the catalog so the customer can choose e-books.
        catalog.display_catalog()
        choice=input("Enter the title of the e-book to add to the cart (or 'checkout' to complete your order, 'remove' to remove an item, 'update' to update quantity): ").strip()

        if choice.lower()=="checkout":
          # End the loop if the customer wants to checkout
            break
        elif choice.lower()=="remove":
          # Remove a specific e-book from the cart.
            title=input("Enter the title of the e-book to remove: ")
            cart.remove_from_cart(title)
        elif choice.lower()=="update":
          # Update the quantity of a specific e-book in the cart
            title=input("Enter the title of the e-book to update quantity: ")
            while True:
                try:
                    quantity=int(input("Enter the new quantity:"))
                    if quantity < 0:
                        print("Quantity must be 0 or more.")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number.")
            cart.update_quantity(title, quantity)
        else:
          # Add an e-book to the cart by title if available
            ebook=catalog.get_ebook_by_title(choice)
            if ebook:
                while True:
                    try:
                        quantity=int(input("Enter quantity:"))
                        if quantity<=0:
                            print("Please enter a positive quantity.")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid number.")
                cart.add_to_cart(ebook, quantity)
                print(f"'{ebook.get_title()}' has been added to your cart.")
            else:
                print("Sorry, this book is not available.")
# Display the final contents of the cart.
    cart.display_cart()

    if len(cart.get_cart_items())==0:
        print("Your cart is empty. No order placed.")
        return
# Create an order and generate the invoice for the customer
    order=Order(cart, customer)
    order.generate_invoice()
# Payment process.
    while True:
        payment_method=input("Enter payment method (Credit Card / ApplePay): ").strip()
        if payment_method.lower() in ["credit card", "applepay"]:
            payment=Payment(order, payment_method)
            payment.process_payment()
            break
        else:
            print("Please enter a valid payment method (Credit Card / ApplePay).")

    print("Thank you for shopping with us!")

# Run the main function
if __name__ == "__main__":
    main()