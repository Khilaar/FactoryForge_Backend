from django.db import models


# Create your models here.
class ClientOrder(models.Model):
    STATUS_CHOICES = [
        (1, 'Created'),
        (2, 'In Progress'),
        (3, 'Quality Control'),
        (4, 'Completed')
    ]

    client = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE)
    products = models.ManyToManyField('product.Product')
    client_note = models.TextField(blank=True)
    due_date = models.DateField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delivery_time = models.DurationField(blank=True)
    processing_time = models.DurationField(blank=True)
    order_status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    nr_products = models.IntegerField()
    nr_products_completed = models.IntegerField()