from rest_framework import serializers
from restfulApi.models import company

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = company
        fields = ('name', 'company_id')
