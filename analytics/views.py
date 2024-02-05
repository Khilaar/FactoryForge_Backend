from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from analytics.models import Analytics
from analytics.serializers import AnalyticsSerializer
from analytics.services import calculate_profit


#######################################################################################################

class ListCreateAnalyticsView(ListCreateAPIView):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
    permission_classes = [IsAuthenticated]

#######################################################################################################

class ProfitView(APIView):
    def get(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        profit = calculate_profit(start_date, end_date)

        return Response({"profit":profit})

#######################################################################################################
