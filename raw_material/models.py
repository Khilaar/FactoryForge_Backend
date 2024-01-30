from django.db import models


# Create your models here.
class RawMaterial(models.Model):
    title = models.CharField(max_length=250)
    quantity = models.IntegerField()
    restock_required = models.BooleanField(default=False)
    max_quantity = models.IntegerField()
    inventory = models.ForeignKey('inventory.Inventory', on_delete=models.PROTECT)
