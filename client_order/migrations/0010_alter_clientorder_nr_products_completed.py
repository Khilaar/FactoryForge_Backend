# Generated by Django 5.0.1 on 2024-02-03 22:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("client_order", "0009_rename_products_clientorder_ordered_products"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientorder",
            name="nr_products_completed",
            field=models.IntegerField(default=0),
        ),
    ]
