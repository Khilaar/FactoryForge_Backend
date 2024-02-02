from django.urls import path

from inventory.views import ListCreateInventoryView, RawMaterialsByInventoryView, RawMaterialDetailView
from product.views import RetrieveUpdateDeleteProduct

urlpatterns = [
    path('', ListCreateInventoryView.as_view()),
    path('<str:inventory_name>', RawMaterialsByInventoryView.as_view(), name='raw_materials_by_inventory'),
    path('<str:inventory_name>/<name>/', RawMaterialDetailView.as_view(), name='raw_material_detail'),
]