from django.db import models
from django.db.models import OneToOneField, TextField


class ProductInventory(models.Model):
    name = models.CharField(max_length=250)
    description = TextField(blank=True, null=True)
    user = OneToOneField('custom_user.CustomUser', on_delete=models.PROTECT)
    last_restock = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'{self.name}'