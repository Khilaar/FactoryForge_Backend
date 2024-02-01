from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from factoryforge.permissions.permissions import ReadOnly
from inventory.models import Inventory
from inventory.serializers import InventorySerializer, RawMaterialSerializer
from raw_material.models import RawMaterial


# Create your views here.
class ListCreateInventoryView(ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated | ReadOnly]

class RawMaterialsByInventoryView(ListAPIView):
    serializer_class = RawMaterialSerializer

    def get_queryset(self):
        inventory_name = self.kwargs['inventory_name']
        return RawMaterial.objects.filter(inventory__name=inventory_name)