from rest_framework import serializers

from raw_material_order.models import RawMaterialOrder


class RawMaterialOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterialOrder
        fields = ['id', 'raw_materials', 'quantity', 'supplier', 'order_date', 'delivery_date', 'status',
                  'raw_materials_order']

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
