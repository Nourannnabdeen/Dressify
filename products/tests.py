from django.test import TestCase
from products.models import Product

class ProductTestCase(TestCase):

    def test_product_creation(self):
        # Create a product
        product = Product.objects.create(
            name='Test Product',
            description='A test product.',
            price=100.00,
            available_sizes="S,M,L,XL"
        )

        # Check if the product was created successfully
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 100.00)
        self.assertEqual(product.available_sizes, "S,M,L,XL")

    def test_product_price(self):
        # Create a product with a negative price
        with self.assertRaises(ValueError):
            Product.objects.create(
                name='Invalid Product',
                description='A product with invalid price.',
                price=-10.00,
                available_sizes="S,M,L"
            )