from django.urls import path
from api import views
from api.views import CompanyList,CompanyDetail,VacancyList,VacancyDetail,VacancyByCompany,VacancyTopTen

urlpatterns = [
    path('companies/',CompanyList.as_view()),
    path('vacancies/',VacancyList.as_view()),
    path('companies/<int:pk>/',CompanyDetail.as_view()),
    path('vacancies/<int:pk>/',VacancyDetail.as_view()),
    path('companies/<int:pk>/vacancies/',VacancyByCompany.as_view()),
    path('vacancies/top_ten/',VacancyTopTen.as_view()),
]