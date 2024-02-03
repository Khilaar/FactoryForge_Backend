from django.db import models

from product_inventory.models import ProductInventory


# Create your models here.
class Product(models.Model):
    STATUS_CHOICES = [
        (1, 'Created'),
        (2, 'In Progress'),
        (3, 'Quality Control'),
        (4, 'Completed')
    ]
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    quantity_available = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    production_status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    production_cost = models.DecimalField(decimal_places=2, max_digits=5)
    category = models.CharField(max_length=250, blank=True, null=True)
    raw_materials = models.ManyToManyField('raw_material.RawMaterial', blank=True)
    raw_material_requirements = models.JSONField(null=True, blank=True)
    inventory = models.ForeignKey(ProductInventory, on_delete=models.PROTECT, related_name='products', null=True, blank=True)

    def __str__(self):
        return self.title