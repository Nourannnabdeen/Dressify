from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

class CustomUserTestCase(TestCase):

    def test_user_creation(self):
        # Create a user
        user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword123',
            email='testuser@example.com'
        )

        # Check if the user was created successfully
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')

        # Check if the created_at field is populated
        self.assertIsNotNone(user.created_at)

    def test_user_password(self):
        # Create a user and check if the password is hashed
        user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword123',
            email='testuser@example.com'
        )
        self.assertTrue(user.check_password('testpassword123'))