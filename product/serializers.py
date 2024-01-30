from rest_framework import serializers

from product.models import Product
from raw_material.models import RawMaterial


class RawMaterialRequirementSerializer(serializers.Serializer):
    raw_material_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'quantity', 'price', 'production_status', 'production_cost', 'category',
                  'raw_materials', 'requirements']

    def create(self, validated_data):
        requirements_data = validated_data.pop('requirements', [])
        product = Product.objects.create(**validated_data)

        if requirements_data:
            for requirement_data in requirements_data:
                raw_material_name = requirement_data['raw_material_name']
                quantity = requirement_data['quantity']
                try:
                    raw_material_id = RawMaterial.objects.values_list('id', flat=True).get(name=raw_material_name)
                except RawMaterial.DoesNotExist:
                    print('RawMaterial does not exist')
                    break
                product.requirements.create(raw_material_id=raw_material_id, quantity=quantity)
        return product

    def update(self, instance, validated_data):
        requirements_data = validated_data.pop('requirements', [])
        instance = super().update(instance, validated_data)

        instance.requirements.all().delete()
        if requirements_data:
            for requirement_data in requirements_data:
                raw_material_name = requirement_data['raw_material_name']
                quantity = requirement_data['quantity']
                try:
                    raw_material_id = RawMaterial.objects.values_list('id', flat=True).get(name=raw_material_name)
                except RawMaterial.DoesNotExist:
                    print('RawMaterial does not exist')
                    break
                instance.requirements.create(raw_material_id=raw_material_id, quantity=quantity)
        return instance
