from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from analytics.services import calculate_profit
from factoryforge.permissions.permissions import ReadOnly
from raw_material.models import RawMaterial
from raw_material.serializers import RawMaterialSerializer


class ListCreateRawMaterialView(ListCreateAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    permission_classes = [IsAuthenticated | ReadOnly]


class RetrieveUpdateDeleteRawMaterialView(RetrieveUpdateDestroyAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    permission_classes = [IsAuthenticated | ReadOnly]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        new_quantity_aviable = serializer.validated_data.get('quantity_aviable', instance.quantity_aviable)
        max_quantity = instance.max_quantity

        if new_quantity_aviable > max_quantity:
            return Response(
                {'error': 'Updating quantity_available would exceed max_quantity'},
                status = status.HTTP_400_BAD_REQUEST
            )

        self.perform_update(serializer)
        return Response(serializer.data)