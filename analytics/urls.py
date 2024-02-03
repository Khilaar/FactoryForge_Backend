from django.urls import path

from analytics.views import ListCreateAnalyticsView
from inventory.views import ListCreateInventoryView

urlpatterns = [
    path('', ListCreateAnalyticsView.as_view()),
]