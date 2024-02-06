import uuid

from django.db import transaction
from rest_framework import serializers

from client_order.models import ClientOrder, OrderedProduct
from custom_user.models import CustomUser
from product.models import Product


class OrderedProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product', write_only=True)

    class Meta:
        model = OrderedProduct
        fields = ['product_name', 'product', 'quantity', 'production_status']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class ClientOrderSerializer(serializers.ModelSerializer):
    ordered_products = OrderedProductSerializer(many=True)

    class Meta:
        model = ClientOrder
        fields = ['id', 'client', 'ordered_products', 'client_note', 'due_date', 'created', 'updated', 'delivery_time',
                  'processing_time', 'order_status', 'nr_products', 'nr_products_completed',
                  'tracking_number']

    def create(self, validated_data):
        if validated_data.client.type_of_user != 'C':
            raise serializers.ValidationError('User is not of type client.')

        ordered_products_data = validated_data.pop('ordered_products', [])
        with transaction.atomic():
            client_order = ClientOrder.objects.create(**validated_data)
            client_order.nr_products = len(ordered_products_data)
            client_order.tracking_number = self.generate_tracking_number(client_order)
            for p in ordered_products_data:
                try:
                    p_name = p['product']
                    p_quantity = p['quantity']
                    product_id = Product.objects.get(title__iexact=p_name)
                except Product.DoesNotExist:
                    raise serializers.ValidationError(f"Product with name {p} does not exist.")
                if p_quantity < 0:
                    raise serializers.ValidationError('Quantity cannot be negative.')
                OrderedProduct.objects.create(client_order=client_order, product=product_id, quantity=p_quantity)
            client_order.save()
        return client_order

    def update(self, instance, validated_data):
        if instance.order_status == 6:
            raise serializers.ValidationError('This order has already been completed.')

        products_data = validated_data.pop('ordered_products', [])

        with transaction.atomic():
            instance = super().update(instance, validated_data)
            user_type = validated_data.get('client')
            if instance.client.type_of_user != 'C' or user_type.type_of_user != 'C':
                raise serializers.ValidationError('User is not of type client.')

            if len(products_data) > 0:
                ordered_products = instance.ordered_products.all()
                ordered_product_ids = [p.id for p in ordered_products]

                for p_data in products_data:
                    p_name = p_data['product']
                    p_quantity = p_data['quantity']

                    try:
                        product = Product.objects.get(title__iexact=p_name)
                    except Product.DoesNotExist:
                        raise serializers.ValidationError(f"Product with name {p_name} does not exist.")

                    if p_quantity < 0:
                        raise serializers.ValidationError('Quantity cannot be negative.')

                    if product.id in ordered_product_ids:
                        ordered_p = OrderedProduct.objects.get(client_order=instance, product=product)
                        ordered_p.quantity = p_quantity
                        ordered_p.save()
                    else:
                        OrderedProduct.objects.create(client_order=instance, product=product, quantity=p_quantity)
                OrderedProduct.objects.filter(client_order=instance).exclude(
                    product__title__in=[p['product'] for p in products_data]).delete()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['client'] = ClientSerializer(instance.client).data
        ordered_products_data = OrderedProduct.objects.filter(client_order=instance.id)
        representation['ordered_products'] = OrderedProductSerializer(ordered_products_data, many=True).data
        return representation

    def generate_tracking_number(self, client_order):
        unique_id = str(uuid.uuid4()).replace('-', '').upper()[:12]
        unique_info = f'{client_order.client.id}'
        tracking_number = f'TN-{unique_info}-{unique_id}'
        return tracking_number
