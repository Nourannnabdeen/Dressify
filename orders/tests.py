from django.test import TestCase
from orders.models import Order, Cart
from products.models import Product
from django.contrib.auth import get_user_model

class OrderTestCase(TestCase):

    def setUp(self):
        # Create a user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a Cart for the order
        self.cart = Cart.objects.create(user=self.user)

        # Create a product to add to the cart
        self.product = Product.objects.create(
            name="Test Product",
            description="A test product.",
            price=100.00,
            available_sizes="S,M,L"
        )

    def test_order_creation(self):
        # Create an order and associate it with the cart
        order = Order.objects.create(
            user=self.user,
            cart=self.cart,
            shipping_address="Test Address",
            billing_address="Test Address",
        )

        # Check if the order is created successfully
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.shipping_address, "Test Address")
        self.assertEqual(order.billing_address, "Test Address")
        self.assertEqual(order.cart, self.cart)