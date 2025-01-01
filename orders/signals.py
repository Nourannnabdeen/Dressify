from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Order

@receiver(post_save, sender=Order)
def notify_on_purchase(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='Order Confirmation',
            message=f'Thank you for ordering {instance.product.name}.',
            from_email='halawaelhaggag@gmail.com',  # Your email
            recipient_list=[instance.user.email],  # Recipient's email
            fail_silently=False,
        )