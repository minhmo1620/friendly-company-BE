from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CompanySerializer
from .models import company
from .company_stats import get_all_charts

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = company.objects.all().order_by('name')
    serializer_class = CompanySerializer

class SearchViewSet(APIView):
    def get(self, request):
        company_name = dict(request.query_params)['company_name'][0]
        approval_rate_over_years, years = get_all_charts(company_name)
        return Response({"hi": approval_rate_over_years}, status=status.HTTP_200_OK)
