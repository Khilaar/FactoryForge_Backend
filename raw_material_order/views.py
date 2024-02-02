from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from factoryforge.permissions.permissions import ReadOnly
from raw_material_order.models import RawMaterialOrder
from raw_material_order.serializers import RawMaterialOrderSerializer


# Create your views here.
class RawMaterialOrderListCreateView(ListCreateAPIView):
    queryset = RawMaterialOrder.objects.all()
    serializer_class = RawMaterialOrderSerializer
    permission_classes = [IsAuthenticated | ReadOnly]


class RetrieveUpdateDeleteRawMaterialOrder(RetrieveUpdateDestroyAPIView):
    queryset = RawMaterialOrder.objects.all()
    serializer_class = RawMaterialOrderSerializer
    permission_classes = [IsAuthenticated | ReadOnly]
    lookup_url_kwarg = 'raw_material_order_id'
