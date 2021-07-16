from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CompanySerializer
from .models import Company
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response  import Response
# Create your view
# class CompanyViewSet(viewsets.ViewSet):
# 	quaryset = Company.objects.all()
# 	serializer_class = CompanySerializer

class CompanyViewSet(viewsets.ViewSet):
	authentication_classesj = [JWTAuthentication,]
	permission_classes = [IsAuthenticated] 

	def list(self, request):
		company = Company.objects.all()
		serializer = CompanySerializer(company,many=True,context={'request':request})
		resp_dict ={'error':False, 'msg':'All comapny data','data':serializer.data}
		return Response(resp_dict)

	def create(self,request):
		try:
			serializer = CompanySerializer(data=request.data,context={'request':request})
			serializer.is_valid()
			company_instance=serializer.save()
			resp_dict = {'error':False, 'msg':'comapny data cerate successfully'}
		except Exception as e:
			print(e)
			resp_dict = {'error':False, 'msg':'error during saving data comapny '}
		return Response(resp_dict)


	def update(self,request,pk=None):
		try:
			quaryset = Company.object.all()
			company = get_object_or_404(quaryset,pk=pk)

			serializer = CompanySerializer(data=request.data,context={'request':request})
			serializer.is_valid()
			company_instance=serializer.save()
			resp_dict ={'error':False, 'msg':'comapny data update successfully'}
		except Exception as e:
			resp_dict ={'error':False, 'msg':'error during update data comapny '}
		return Response(resp_dict)



company_list = CompanyViewSet.as_view({'get':'list'})
company_create = CompanyViewSet.as_view({'post':'create'})
company_update = CompanyViewSet.as_view({'put':'update'})