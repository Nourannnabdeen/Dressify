from django.db import models
from django.conf import settings

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.email}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)  # String reference to avoid circular import
    quantity = models.PositiveIntegerField(default=1)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    shipping_address = models.TextField()
    billing_address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = sum(
                item.product.price * item.quantity for item in self.cart.items.all()
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')  # String reference
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)  # String reference
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"