from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from raw_material.models import RawMaterial


class ListCreateRawMaterialView(ListCreateAPIView):
    queryset = RawMaterial.objects.all()


class RetrieveUpdateDeleteRawMaterialView(RetrieveUpdateDestroyAPIView):
    queryset = RawMaterial.objects.all()
