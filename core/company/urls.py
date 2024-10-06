# core/company/urls.py
from django.urls import path
from .views import CompanyListCreate, CompanyDetail

urlpatterns = [
    path('companies/', CompanyListCreate.as_view(), name='company-list-create'),
    path('companies/<uuid:pk>/', CompanyDetail.as_view(), name='company-detail'),
]
