from rest_framework import serializers

from product.models import Product
from raw_material.models import RawMaterial


class RawMaterialRequirementSerializer(serializers.Serializer):
    raw_material_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'quantity_available', 'price', 'production_status', 'production_cost',
                  'category', 'raw_materials', 'requirements']

    def create(self, validated_data):
        requirements_data = validated_data.pop('requirements', [])
        product = Product.objects.create(**validated_data)

        if requirements_data:
            for raw_material_name, quantity in requirements_data:
                try:
                    raw_material_id = RawMaterial.objects.get(name=raw_material_name)
                except RawMaterial.DoesNotExist:
                    raise serializers.ValidationError(f'RawMaterial "{raw_material_name}" does not exist')
                requirements_data[raw_material_id] = quantity
                del requirements_data[raw_material_name]
        product.requirements = requirements_data
        product.save()
        return product

    def update(self, instance, validated_data):
        requirements_data = validated_data.pop('requirements', [])
        instance = super().update(instance, validated_data)

        if requirements_data:
            for raw_material_name, quantity in requirements_data:
                try:
                    raw_material_id = RawMaterial.objects.get(name=raw_material_name)
                except RawMaterial.DoesNotExist:
                    raise serializers.ValidationError(f'RawMaterial "{raw_material_name}" does not exist')
                requirements_data[raw_material_id] = quantity
                del requirements_data[raw_material_name]
        instance.requirements = requirements_data
        instance.save()
        return instance
