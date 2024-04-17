from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status,mixins,generics

import json
from ..models import Company,Vacancy
from ..serializers import CompanySerializer,VacancySerializer,CompanySerializer2,VacancySerializer2


class CompanyList(generics.ListCreateAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer2

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer2

class VacancyList(generics.ListCreateAPIView):
    queryset=Vacancy.objects.all()
    serializer_class=VacancySerializer
    
class VacancyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Vacancy.objects.all()
    serializer_class=VacancySerializer

class VacancyByCompany(generics.ListAPIView):
    serializer_class=VacancySerializer
    def get_queryset(self):
        try:
            company = Company.objects.get(id=self.kwargs['pk'])
            return Vacancy.objects.filter(company=company)
        except Company.DoesNotExist as e:
            return Vacancy.objects.none()
    
class VacancyTopTen(generics.ListAPIView):
    queryset=Vacancy.objects.order_by('-salary')[:10]
    serializer_class=VacancySerializer