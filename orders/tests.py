from django.test import TestCase
from orders.models import Order
from users.models import CustomUser

class OrderModelTest(TestCase):
    def test_create_order(self):
        user = CustomUser.objects.create_user(
            username='testuser', email='test@example.com', password='testpassword'
        )
        order = Order.objects.create(user=user, shipping_address="123 Test St", billing_address="123 Test St", total_price=100.00)
        self.assertEqual(order.user.username, 'testuser')
        self.assertEqual(order.total_price, 100.00)