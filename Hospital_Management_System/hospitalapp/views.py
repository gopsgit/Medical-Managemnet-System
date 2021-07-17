from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CompanySerializer
from .serializer import ComapnyBankSerializer
from .models import Company,CompanyBank
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response  import Response
from rest_framework import generics


class CompanyViewSet(viewsets.ViewSet):
	authentication_classesj = (JWTAuthentication,)
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
			quaryset = Company.objects.all()
			company = get_object_or_404(quaryset,pk=pk)
			serializer = CompanySerializer(data=request.data,context={'request':request})
			serializer.is_valid()
			company_instance=serializer.save()
			resp_dict ={'error':False, 'msg':'comapny data update successfully'}
		except Exception as e:
			print(e)
			resp_dict ={'error':False, 'msg':'error during update data comapny '}
		return Response(resp_dict)

# Comapny Bank Viewset
class CompanyBankViewSet(viewsets.ViewSet):
	authentication_classesj = [JWTAuthentication,]
	permission_classes = [IsAuthenticated] 


	def list(self, request):
		company_bank= CompanyBank.objects.all()
		serializer = ComapnyBankSerializer(company_bank,many=True,context={'request':request})
		resp_dict ={'error':False, 'msg':'All comapnyBank data','data':serializer.data}
		return Response(resp_dict)


	# create method
	def create(self,request):

		try:
			serializer = ComapnyBankSerializer(data=request.data,context={'request':request})
			serializer.is_valid()
			company_instance=serializer.save()
			resp_dict = {'error':False, 'msg':'comapany bank data cerate successfully'}
		except Exception as e:
			print(e)
			resp_dict = {'error':False, 'msg':'error during saving data comapnyBank Data '}
		return Response(resp_dict)

		# single data retrive
	def retrive(self,request,pk=None):
		try:
			quaryset = CompanyBank.objects.all()
			company_bank = get_object_or_404(quaryset,pk=pk)
			serializer = ComapnyBankSerializer(data=request.data,context={'request':request})
			resp_dict ={'error':False, 'msg':'Single CompanyBank data fetch successfully'}
		except Exception as e:
			print(e)
			resp_dict ={'error':False, 'msg':'error during Single CompanyBank data fetch '}
		return Response(resp_dict)


		#update companyBank data
	def update(self,request,pk=None):
		try:
			quaryset = CompanyBank.objects.all()
			company = get_object_or_404(quaryset,pk=pk)
			serializer = ComapnyBankSerializer(data=request.data,context={'request':request})
			serializer.is_valid()
			company_instance=serializer.save()
			resp_dict ={'error':False, 'msg':'comapny Bankdata update successfully'}
		except Exception as e:
			print(e)
			resp_dict ={'error':False, 'msg':'error during update data comapny Bankdata'}
		return Response(resp_dict)


#filter by comapny name
class CompanyNameViewSet(generics.ListCreateAPIView):
	authentication_classesj = [JWTAuthentication,]
	permission_classes = [IsAuthenticated] 
	serializer_class = CompanySerializer
	def get_queryset(self):
		name = self.kwargs['pk']
		return Company.objects.filter(name=name)

	





company_list = CompanyViewSet.as_view({'get':'list'})
company_create = CompanyViewSet.as_view({'post':'create'})
company_update = CompanyViewSet.as_view({'put':'update'})
# for CompanyBank 
company_bank_create = CompanyBankViewSet.as_view({'post':'create'})
company_bank_list = CompanyViewSet.as_view({'get':'list'})
company_bank_single = CompanyViewSet.as_view({'get':'list'})
company__bank_update = CompanyViewSet.as_view({'put':'update'})

