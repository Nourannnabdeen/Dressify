from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def notify_on_purchase(sender, instance, created, **kwargs):
    if created:
        print(f"Order created for product: {instance.product.name}")
        # Send an email or update another system here