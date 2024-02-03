from rest_framework import serializers

from custom_user.models import CustomUser
from raw_material_order.models import RawMaterialOrder


class CustomSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'type_of_user')


class RawMaterialOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterialOrder
        fields = ['id', 'raw_materials', 'quantity', 'supplier', 'order_date', 'delivery_date', 'status',
                  'raw_materials_order']

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['supplier'] = CustomSupplierSerializer(instance.supplier).data
        return representation
