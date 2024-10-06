# core/jobopening/urls.py
from django.urls import path
from .views import JobOpeningListCreate, JobOpeningDetail

urlpatterns = [
    path('jobs/', JobOpeningListCreate.as_view(), name='job-list-create'),
    path('jobs/<uuid:pk>/', JobOpeningDetail.as_view(), name='job-detail'),
]
