from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from raw_material.models import RawMaterial
from raw_material.serializers import RawMaterialSerializer, CreateRawMaterialSerializer


class ListCreateRawMaterialView(ListCreateAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer

    # if 'METHOD' == 'POST':
    #     serializer_class = CreateRawMaterialSerializer
    # else:
    #     serializer_class = RawMaterialSerializer


class RetrieveUpdateDeleteRawMaterialView(RetrieveUpdateDestroyAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
