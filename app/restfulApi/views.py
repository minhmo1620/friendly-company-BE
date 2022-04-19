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
        all_stats = get_all_charts(company_name)
        return Response({"data": all_stats}, status=status.HTTP_200_OK)

class FilterViewSet(APIView):
    def get(self, request):
        query_params = dict(request.query_params)
        job_industry = query_params['job_industry'][0]
        state = query_params['state'][0]
        city = query_params['city'][0]
        job_type = query_params['job_type'][0]

        companies = [
            {
                "name": "Google",
                "approval_rate": "99",
                "wage_range": [100, 200]
            },
            {
                "name": "Facebook",
                "approval_rate": "99",
                "wage_range": [100, 200]
            }
        ]
        return Response({"companies": companies}, status=status.HTTP_200_OK)
