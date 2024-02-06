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


"""
def estimate(request):
    raw_materials_data = request.data.get('raw_materials', [])

    for raw_material_data in raw_materials_data:
        raw_material_id = raw_material_data['raw_material_id']
        required_quantity = raw_material_data['quantity']

        # Calculate the minimum quantity based on available raw materials
        available_quantity = RawMaterial.objects.filter(id=raw_material_id).aggregate(Sum('quantity'))[
                                 'quantity__sum'] or 0
        current_min_quantity = available_quantity // required_quantity

        # Update min_quantity if it's None or the current_min_quantity is smaller
        min_quantity = min_quantity if min_quantity is not None and min_quantity < current_min_quantity else current_min_quantity

    return Response({'min_quantity': min_quantity}, status=status.HTTP_200_OK)
"""
