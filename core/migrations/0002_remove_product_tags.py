# Generated by Django 4.2.11 on 2024-03-18 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="tags",
        ),
    ]