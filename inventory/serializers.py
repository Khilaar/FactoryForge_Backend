from rest_framework import serializers

from inventory.models import Inventory
from raw_material.models import RawMaterial


#######################################################################################################
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'description', 'user', 'last_restock']

#######################################################################################################

class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = ['id', 'name', 'restock_required', 'max_quantity', 'inventory']

#######################################################################################################

