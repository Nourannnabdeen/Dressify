from django.test import TestCase
from .models import Product, Category

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category", description="A test category")
        self.product = Product.objects.create(
            name="Test Product",
            description="A test product",
            price=10.99,
            quantity=5,
            category=self.category,  # Add this
        )

    def test_product_creation(self):
        """Test if the product is created successfully."""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 10.99)
        self.assertEqual(self.product.category.name, "Test Category")