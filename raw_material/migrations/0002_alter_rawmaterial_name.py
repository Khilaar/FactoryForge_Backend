# Generated by Django 5.0.1 on 2024-02-06 23:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("raw_material", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rawmaterial",
            name="name",
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
