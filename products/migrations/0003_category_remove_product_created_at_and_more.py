# Generated by Django 5.1.4 on 2024-12-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_product_created_at_product_updated_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="product",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
        migrations.RemoveField(
            model_name="product",
            name="quantity",
        ),
        migrations.RemoveField(
            model_name="product",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="product",
            name="available_sizes",
            field=models.CharField(default="Default Size", max_length=255),
            preserve_default=False,
        ),
    ]
