from django.urls import path

from analytics.views import ListCreateAnalyticsView

urlpatterns = [
    path('', ListCreateAnalyticsView.as_view()),
]