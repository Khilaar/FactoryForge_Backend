# Generated by Django 5.0.1 on 2024-01-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("client_order", "0004_alter_clientorder_client_note"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientorder",
            name="delivery_time",
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="clientorder",
            name="due_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="clientorder",
            name="processing_time",
            field=models.DurationField(blank=True, null=True),
        ),
    ]
