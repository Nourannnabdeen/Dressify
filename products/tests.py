from django.test import TestCase
from products.models import Product

class ProductModelTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(name="Test Product", price=25.99, description="A cool T-shirt")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 25.99)