from django.test import TestCase
from orders.models import Order
from users.models import CustomUser
from products.models import Product
from decimal import Decimal

class OrderTestCase(TestCase):

    def test_order_creation(self):
        # Create a user and product
        user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword123',
            email='testuser@example.com'
        )
        product = Product.objects.create(
            name='Test Product',
            description='A test product.',
            price=100.00,
            available_sizes="S,M,L,XL"
        )

        # Create an order for the user
        order = Order.objects.create(
            user=user,
            shipping_address='Test Shipping Address',
            billing_address='Test Billing Address'
        )

        # Add product to order
        order.total_price = Decimal(product.price)
        order.save()

        # Check if the order is created successfully
        self.assertEqual(order.user, user)
        self.assertEqual(order.total_price, Decimal(100.00))
        self.assertEqual(order.shipping_address, 'Test Shipping Address')