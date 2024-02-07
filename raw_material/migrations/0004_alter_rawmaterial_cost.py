# Generated by Django 5.0.1 on 2024-02-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("raw_material", "0003_alter_rawmaterial_cost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rawmaterial",
            name="cost",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=5, null=True
            ),
        ),
    ]