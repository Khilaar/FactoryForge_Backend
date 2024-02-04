# Generated by Django 5.0.1 on 2024-02-02 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0008_remove_product_inventory"),
        ("product_inventory", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="inventory",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product",
                to="product_inventory.productinventory",
            ),
        ),
    ]
