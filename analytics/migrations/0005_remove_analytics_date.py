# Generated by Django 5.0.1 on 2024-02-07 18:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("analytics", "0004_analytics_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="analytics",
            name="date",
        ),
    ]