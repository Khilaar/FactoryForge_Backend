from django.db import models
from django.db.models import OneToOneField


# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    user = OneToOneField('custom_user.CustomUser', on_delete=models.PROTECT)
    last_restock = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'{self.name}'


