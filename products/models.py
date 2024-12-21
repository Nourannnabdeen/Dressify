from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_sizes = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)  # Add the 'quantity' field

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")

    def __str__(self):
        return self.name