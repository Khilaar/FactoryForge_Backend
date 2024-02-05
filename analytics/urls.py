from django.urls import path

from analytics.views import ListCreateAnalyticsView, ProfitView

urlpatterns = [
    path('', ListCreateAnalyticsView.as_view()),
    path('profit/', ProfitView.as_view())
]