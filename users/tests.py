from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTest(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            username='testuser', email='test@example.com', password='testpassword'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            username='admin', email='admin@example.com', password='adminpassword'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)