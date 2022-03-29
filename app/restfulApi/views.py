from rest_framework import viewsets

from .serializers import CompanySerializer
from .models import company

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = company.objects.all().order_by('name')
    serializer_class = CompanySerializer