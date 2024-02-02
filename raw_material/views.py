from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from raw_material.models import RawMaterial
from raw_material.serializers import RawMaterialSerializer


class ListCreateRawMaterialView(ListCreateAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer


class RetrieveUpdateDeleteRawMaterialView(RetrieveUpdateDestroyAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
