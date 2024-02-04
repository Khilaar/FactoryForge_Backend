from rest_framework import serializers

from raw_material.models import RawMaterial


class RawMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = RawMaterial
        fields = ['id', 'name', 'quantity_available', 'restock_required', 'inventory']


class CreateRawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = ['id', 'name', 'quantity_available', 'restock_required', 'inventory']
