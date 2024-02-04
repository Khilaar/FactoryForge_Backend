from django.db import models


# Create your models here.
class RawMaterial(models.Model):
    name = models.CharField(max_length=250)
    quantity_available = models.IntegerField(default=0)
    restock_required = models.BooleanField(default=False)
    max_quantity = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    inventory = models.ForeignKey('inventory.Inventory', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name