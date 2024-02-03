from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from analytics.models import Analytics
from analytics.serializers import AnalyticsSerializer


# Create your views here.
class ListCreateAnalyticsView(ListCreateAPIView):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
    permission_classes = [IsAuthenticated]