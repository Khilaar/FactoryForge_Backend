from rest_framework import serializers

from inventory.serializers import InventorySerializer
from raw_material.models import RawMaterial


class RawMaterialSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer()

    class Meta:
        model = RawMaterial
        fields = ['id', 'name', 'quantity_available', 'restock_required', 'inventory']


class CreateRawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'
