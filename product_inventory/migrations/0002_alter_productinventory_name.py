# Generated by Django 5.0.1 on 2024-02-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product_inventory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productinventory",
            name="name",
            field=models.CharField(default="product_inventory", max_length=250),
        ),
    ]