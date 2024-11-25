# Generated by Django 4.2.11 on 2024-04-10 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_product_new"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="old_price",
            field=models.DecimalField(
                decimal_places=2, default="2.99", max_digits=5, null=True
            ),
        ),
    ]