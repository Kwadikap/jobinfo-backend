# core/location/urls.py
from django.urls import path
from .views import LocationListCreate, LocationDetail

urlpatterns = [
    path('locations/', LocationListCreate.as_view(), name='location-list-create'),
    path('locations/<uuid:pk>/', LocationDetail.as_view(), name='location-detail'),
]
