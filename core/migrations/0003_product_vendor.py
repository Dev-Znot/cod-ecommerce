# Generated by Django 4.2.11 on 2024-03-19 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_product_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="vendor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.vendor",
            ),
        ),
    ]