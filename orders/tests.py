from django.test import TestCase
from products.models import Product, Category
from orders.models import Order, Cart
from django.contrib.auth import get_user_model
from io import StringIO
from contextlib import redirect_stdout

User = get_user_model()

class CartModelTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username="testuser", password="testpassword")

        # Create a category
        self.category = Category.objects.create(name="Test Category", description="Test description")

        # Create products
        self.product1 = Product.objects.create(
            name="Product 1",
            description="Description for product 1",
            price=10.99,
            available_sizes="S, M, L",
            category=self.category,
        )
        self.product2 = Product.objects.create(
            name="Product 2",
            description="Description for product 2",
            price=15.99,
            available_sizes="M, L, XL",
            category=self.category,
        )

        # Create a cart
        self.cart = Cart.objects.create(user=self.user)

    def test_add_products_to_cart(self):
        # Add products to the cart
        self.cart.products.add(self.product1, self.product2)

        # Check if the products are in the cart
        self.assertIn(self.product1, self.cart.products.all())
        self.assertIn(self.product2, self.cart.products.all())

    def test_cart_representation(self):
        # Check the string representation of the cart
        self.assertEqual(str(self.cart), f"Cart of {self.user.username}")