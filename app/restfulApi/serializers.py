from rest_framework import serializers
from restfulApi.models import company, company_data

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = company
        fields = ('name', 'company_id')

class CompanyDataSerializer (serializers.ModelSerializer):
    class Meta: 
        model = company_data
        fields = ['entry_id', 'company_name', 'state', 'job_industry', 'full_time', 'min_average', 'max_average', 'average', 'approval_rate']