# Generated by Django 5.0.1 on 2024-02-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analytics", "0005_remove_analytics_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analytics",
            name="name",
            field=models.CharField(default=None, max_length=200),
        ),
    ]
