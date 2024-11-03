import unittest
from catalog import Catalog
from customer import Customer
from ebook import Ebook
from shopping_cart import ShoppingCart
from order import Order
from payment import Payment

class TestEbookStore(unittest.TestCase):

    def setUp(self):
        # Initial setup before each test
        self.catalog=Catalog()
        self.cart=ShoppingCart()
        self.customer=Customer("Nasser", "123456789@zu.ac.ae", loyalty_member=True)
        self.ebook1=Ebook("From Rags to Riches: A Story of Abu Dhabi", "Mohammed Al Fahim", "June 9, 1995", "History, Nonfiction, Biography", 300)
        self.ebook2=Ebook("Sheikh Zayed: An Eternal Legacy", "Myrna Ayad", "November 2021", "Art, Biography, History", 1000)
        self.catalog.add_ebook(self.ebook1)
        self.catalog.add_ebook(self.ebook2)

    def test_add_ebook_to_catalog(self):
        # Check that catalog initially contains the specific e-books
        self.assertIsNotNone(self.catalog.get_ebook_by_title("From Rags to Riches: A Story of Abu Dhabi"))
        self.assertIsNotNone(self.catalog.get_ebook_by_title("Sheikh Zayed: An Eternal Legacy"))
        # Add a new e-book
        new_ebook = Ebook("Zayed University", "Nasser Almazrouei", "2024", "Nonfiction", 190)
        self.catalog.add_ebook(new_ebook)
        # Verify that the new e-book can be found by title
        self.assertIsNotNone(self.catalog.get_ebook_by_title("Zayed University"))

    def test_add_ebook_to_cart(self):
        # Test adding an e-book to the cart
        self.cart.add_to_cart(self.ebook1, 2)
        self.assertIn(self.ebook1, self.cart.get_cart_items())
        self.assertEqual(self.cart.get_cart_items()[self.ebook1], 2)

    def test_remove_ebook_from_cart(self):
        # Test removing an e-book from the cart
        self.cart.add_to_cart(self.ebook1, 1)
        self.cart.remove_from_cart("From Rags to Riches: A Story of Abu Dhabi")
        self.assertNotIn(self.ebook1, self.cart.get_cart_items())

    def test_update_cart_quantity(self):
        # Test updating quantity of an e-book in the cart
        self.cart.add_to_cart(self.ebook1, 1)
        self.cart.update_quantity("From Rags to Riches: A Story of Abu Dhabi", 3)
        self.assertEqual(self.cart.get_cart_items()[self.ebook1], 3)

    def test_loyalty_discount(self):
        # Test applying loyalty discount for a customer
        self.cart.add_to_cart(self.ebook1, 1)
        order=Order(self.cart, self.customer)

        # Calculate expected total with combined loyalty discount and VAT
        subtotal=self.ebook1.get_price()  # Price for one item
        loyalty_discount=0.10
        discount=subtotal*loyalty_discount
        vat=(subtotal-discount)*0.08
        expected_total=subtotal-discount+vat

        self.assertAlmostEqual(order.calculate_total(), expected_total, places=2)

    def test_bulk_discount(self):
        # Test bulk discount by adding 5 items
        self.cart.add_to_cart(self.ebook1, 5)
        order=Order(self.cart, self.customer)

        # Calculate expected total with combined loyalty and bulk discounts and VAT
        subtotal=self.ebook1.get_price() * 5  # Price for five items
        loyalty_discount=0.10
        bulk_discount=0.20
        discount=subtotal*(loyalty_discount+bulk_discount)  # Combined discount of 30%
        vat=(subtotal-discount)*0.08
        expected_total=subtotal-discount+vat

        self.assertAlmostEqual(order.calculate_total(), expected_total, places=2)

    def test_generate_invoice(self):
        # Test invoice generation for an order
        self.cart.add_to_cart(self.ebook1, 1)
        order=Order(self.cart, self.customer)
        order.generate_invoice()  # Should print the invoice details

    def test_payment_process(self):
        # Test payment processing
        self.cart.add_to_cart(self.ebook1, 1)
        order=Order(self.cart, self.customer)
        payment=Payment(order, "ApplePay")
        self.assertEqual(payment.__str__(), f"Payment of {order.calculate_total()} AED via ApplePay")

if __name__ == '__main__':
    unittest.main()