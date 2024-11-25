# Generated by Django 4.2.11 on 2024-05-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coupons",
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
                ("series", models.IntegerField(default=0)),
                ("tag", models.CharField(max_length=50)),
            ],
        ),
    ]