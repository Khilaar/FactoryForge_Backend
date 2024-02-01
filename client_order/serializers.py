import uuid

from rest_framework import serializers

from client_order.models import ClientOrder
from custom_user.models import CustomUser
from product.models import Product


class ProductQuantitySerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'email')


class CustomProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title')


class ClientOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientOrder
        fields = ['id', 'client', 'products', 'client_note', 'due_date', 'created', 'updated', 'delivery_time',
                  'processing_time', 'order_status', 'nr_products', 'nr_products_completed', 'order_and_quantities',
                  'tracking_number']

    def create(self, validated_data):
        order_data = validated_data.pop('order_and_quantities', [])
        product_ids = validated_data.pop('products', [])

        client_order = ClientOrder.objects.create(**validated_data)
        client_order.tracking_number = self.generate_tracking_number(client_order)

        specifics = {}
        if client_order.client.type_of_user != 'C':
            raise serializers.ValidationError('User is not of type client.')
        if not order_data:
            raise serializers.ValidationError('Order not defined.')

        client_order.products.set(product_ids)

        for product_name, quantity in order_data.items():
            try:
                product_id = Product.objects.get(title=product_name).id
            except Product.DoesNotExist:
                raise serializers.ValidationError(f'Product "{product_name}" does not exist.')

            specifics[product_id] = quantity
        client_order.order_and_quantities = specifics
        client_order.save()
        return client_order

    def update(self, instance, validated_data):
        order_data = validated_data.pop('order_and_quantities', [])
        instance = super().update(instance, validated_data)
        order_quantities_update = {}
        if instance.client.type_of_user != 'C':
            raise serializers.ValidationError('User is not of type client.')
        if not order_data:
            raise serializers.ValidationError('Order not defined.')

        for product_name, quantity in order_data.items():
            try:
                product_id = Product.objects.get(title=product_name).id
            except Product.DoesNotExist:
                raise serializers.ValidationError(f'Product "{product_name}" does not exist.')

            order_quantities_update[product_id] = quantity

        instance.order_and_quantities = order_quantities_update
        instance.save()

        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['client'] = ClientSerializer(instance.client).data
        representation['products'] = CustomProductSerializer(instance.products.all(), many=True).data
        return representation

    def generate_tracking_number(self, client_order):
        unique_id = str(uuid.uuid4()).replace('-', '').upper()[:12]
        unique_info = f'{client_order.client.id}'
        tracking_number = f'TN-{unique_info}-{unique_id}'
        return tracking_number
