# Generated by Django 5.0.1 on 2024-02-01 15:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("raw_material", "0002_rename_title_rawmaterial_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rawmaterial",
            old_name="quantity",
            new_name="quantity_available",
        ),
    ]
