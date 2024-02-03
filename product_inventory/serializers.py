from rest_framework import serializers

from product_inventory.models import ProductInventory


class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = ['id', 'name', 'description', 'user', 'last_restock']