from rest_framework import serializers

from analytics.models import Analytics


class AnalyticsSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Analytics
        fields = ['name', 'date', 'description', 'user', 'inventory', 'product_inventory', 'client_orders', 'raw_material_orders']

