# Generated by Django 5.0.1 on 2024-02-03 22:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analytics", "0003_rename_product_analytics_product_inventory"),
    ]

    operations = [
        migrations.AddField(
            model_name="analytics",
            name="name",
            field=models.CharField(default="Analytics", max_length=200),
        ),
    ]
