from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CompanySerializer, CompanyDataSerializer
from .models import company, company_data
from .company_stats import get_all_charts
from .load_heavy_data import get_company_stats_compilation_data

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

        companies = get_companies_list(job_industry, state, city, job_type)
        return Response({"companies": companies}, status=status.HTTP_200_OK)

def get_companies_list(job_industry, state, city, job_type):
    job_type = job_type == 'Full-time'
    # Filter all companies with job_industry, state, city, job_type
    companies_lst = company_data.objects.filter(
        full_time = job_type,
        state = state,
        job_industry = job_industry
    )
    companies = []
    for company in companies_lst:
        entry = {}
        entry['name'] = getattr(company, 'company_name')
        entry['approval_rate'] = getattr(company, 'approval_rate')
        entry['wage_range'] = [getattr(company, 'min_average'), getattr(company, 'max_average')]
        entry['average_wage'] = getattr(company, 'average')

        companies.append(entry)

    return companies

