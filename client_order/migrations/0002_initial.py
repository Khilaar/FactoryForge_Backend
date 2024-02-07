# Generated by Django 5.0.1 on 2024-02-07 20:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client_order', '0001_initial'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='clientorder',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='client_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_order.clientorder'),
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='clientorder',
            name='ordered_products',
            field=models.ManyToManyField(blank=True, related_name='client_orders', through='client_order.OrderedProduct', to='product.product'),
        ),
    ]
