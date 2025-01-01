from decimal import Decimal
from django.test import TestCase
from products.models import Product
from orders.models import Order  # Correct import

class OrderTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            price=Decimal("29.99"),
            sizes="S, M, L",  # Use the correct field name here
            description="A test product description",
        )
        self.order = Order.objects.create(
            user=None,  # Replace with a valid user if applicable
            total_price=Decimal("29.99"),
        )
        self.order.products.add(self.product)
    
    def test_order_creation(self):
        self.assertEqual(self.order.total_price, Decimal("29.99"))
        self.assertIn(self.product, self.order.products.all())