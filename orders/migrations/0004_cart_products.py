# Generated by Django 5.1.4 on 2025-01-02 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_product"),
        ("products", "0007_product_category_product_image_product_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="products",
            field=models.ManyToManyField(related_name="carts", to="products.product"),
        ),
    ]
