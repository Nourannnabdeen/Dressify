from django.test import TestCase
from products.models import Product
from orders.models import Order, Cart
from django.contrib.auth import get_user_model
from io import StringIO
from contextlib import redirect_stdout

class OrderSignalTest(TestCase):
    def setUp(self):
        # Create a user
        User = get_user_model()
        self.user = User.objects.create_user(
    username="testuser",  # Add a username
    email="testuser@example.com",
    password="testpassword",
)
        # Create a product
        self.product = Product.objects.create(
    name="Test Product",
    price=29.99,
    description="Test Description",
    available_sizes="S, M, L",  # Correct field name
)

        # Create a cart
        self.cart = Cart.objects.create(user=self.user)

    def test_order_signal(self):
        # Redirect stdout to capture the signal output
        output = StringIO()
        with redirect_stdout(output):
            # Create an order (this should trigger the signal)
            Order.objects.create(
                user=self.user,
                cart=self.cart,
                shipping_address="123 Test Street",
                billing_address="123 Test Street",
            )

        # Check if the signal printed the correct message
        self.assertIn("Order created for product:", output.getvalue())