from django.db import models


# Create your models here.
class ClientOrder(models.Model):
    STATUS_CHOICES = [
        (1, 'Created'),
        (2, 'In Progress'),
        (3, 'Quality Control'),
        (4, 'Ready for Shipping'),
        (5, 'In Transit'),
        (6, 'Completed')
    ]

    client = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE)
    ordered_products = models.ManyToManyField('product.Product', blank=True)
    client_note = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delivery_time = models.DurationField(blank=True, null=True)
    processing_time = models.DurationField(blank=True, null=True)
    order_status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    nr_products = models.IntegerField()
    nr_products_completed = models.IntegerField()
    order_and_quantities = models.JSONField(null=True, blank=True)
    tracking_number = models.CharField(max_length=250, blank=True, null=True)
