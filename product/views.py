from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from factoryforge.permissions.permissions import ReadOnly
from product.models import Product
from product.serializers import ProductSerializer
from raw_material.models import RawMaterial


class ListCreateProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated | ReadOnly]


class RetrieveUpdateDeleteProduct(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated | ReadOnly]
    lookup_url_kwarg = 'product_id'
