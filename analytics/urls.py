from django.urls import path

from analytics.views import ListCreateAnalyticsView, ProfitView, SoldProductsView, UsedRawMaterialView

urlpatterns = [
    path('', ListCreateAnalyticsView.as_view()),
    path('profit/', ProfitView.as_view()),
    path('soldproducts/', SoldProductsView.as_view()),
    path('usedrawmaterials/', UsedRawMaterialView.as_view())
]