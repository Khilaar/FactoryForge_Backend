# Generated by Django 5.0.1 on 2024-02-02 17:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("raw_material_order", "0002_alter_rawmaterialorder_delivery_date_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rawmaterialorder",
            old_name="raw_material",
            new_name="raw_materials",
        ),
        migrations.RenameField(
            model_name="rawmaterialorder",
            old_name="order",
            new_name="raw_materials_order",
        ),
    ]
