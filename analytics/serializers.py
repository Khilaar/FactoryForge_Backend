from rest_framework import serializers

from analytics.models import Analytics
from client_order.serializers import ClientOrderSerializer


class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytics
        fields = ['name', 'date', 'description', 'user', 'inventory', 'product_inventory', 'client_orders']