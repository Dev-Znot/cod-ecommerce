# Generated by Django 5.0.6 on 2024-11-28 05:23

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_product_freight_alter_product_old_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='category.jpg', null=True, upload_to=core.models.user_directory_path),
        ),
    ]
