# Generated by Django 5.2 on 2025-05-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rueruprechner", "0003_alter_contract_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="notes",
            field=models.TextField(default="", verbose_name="Personal Notes"),
        ),
    ]
