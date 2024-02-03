from rest_framework import serializers

from analytics.models import Analytics


class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytics
        fields = ['name', 'date', 'description', 'user', 'inventory', 'product_inventory']