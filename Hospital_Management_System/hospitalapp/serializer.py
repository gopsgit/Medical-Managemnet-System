from rest_framework import serializers
from .models import Company
from .models import CompanyBank

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = '__all__'

class ComapnyBankSerializer(serializers.ModelSerializer):
	class Meta:
		model = CompanyBank
		fields = '__all__'
	
	def to_representation (self,instance):
		response = super().to_representation(instance)
		response['company'] = CompanySerializer(instance.company_id).data
		return response
