from django.test import TestCase
from django.core.exceptions import ValidationError
from products.models import Product

class ProductTestCase(TestCase):

    def test_product_creation(self):
        # Create a product, including the missing 'quantity' field
        product = Product.objects.create(
            name='Test Product',
            description='A test product.',
            price=100.00,
            available_sizes="S,M,L,XL",
            quantity=10  # Provide a value for the quantity field
        )

        # Check if the product was created successfully
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 100.00)
        self.assertEqual(product.available_sizes, "S,M,L,XL")
        self.assertEqual(product.quantity, 10)  # Check if quantity was set correctly

    def test_product_price(self):
        # Create a product with invalid price
        product = Product(name='Invalid Product', description='Product with invalid price.', price=-10.00, available_sizes="S,M,L")

        # Check if the ValidationError is raised when the price is negative
        with self.assertRaises(ValidationError):
            product.clean()