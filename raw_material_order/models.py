from django.db import models


# Create your models here.
class RawMaterialOrder(models.Model):
    STATUS_CHOICES = [
        (1, 'Ordered'),
        (2, 'In Transit'),
        (3, 'Delivered')
    ]

    supplier = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE)
    raw_material = models.ManyToManyField('raw_material.RawMaterial')
    quantity = models.IntegerField()
    order = models.JSONField(null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return self.supplier
