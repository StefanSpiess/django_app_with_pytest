# Generated by Django 5.2 on 2025-05-03 14:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rueruprechner", "0004_alter_contract_notes"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vendor",
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
                ("name", models.CharField(max_length=120, unique=True)),
                (
                    "vileness",
                    models.CharField(
                        choices=[
                            ("Unknown", "Unknown"),
                            ("Mostly honest", "Mostly Honest"),
                            ("Pretty vile", "Pretty Vile"),
                            ("Pure evil", "Pure Evil"),
                        ],
                        default="Unknown",
                    ),
                ),
                (
                    "last_update",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("notes", models.TextField(default="", verbose_name="Personal Notes")),
            ],
        ),
    ]
