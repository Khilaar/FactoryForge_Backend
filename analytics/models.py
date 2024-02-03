from django.db import models
from django.db.models import OneToOneField


# Create your models here.
class Analytics(models.Model):
    name = models.CharField(max_length=200, default="Analytics")
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey('custom_user.CustomUser', on_delete=models.PROTECT)
    inventory = models.ForeignKey('inventory.Inventory', on_delete=models.PROTECT)
    product_inventory = models.ForeignKey('product_inventory.ProductInventory', on_delete=models.PROTECT)

    def __str__(self):
        return f'Analytics {self.date}'

