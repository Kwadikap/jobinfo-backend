# core/jobopening/views.py
from rest_framework import generics
from core.models import JobOpening
from .serializers import JobOpeningSerializer

class JobOpeningListCreate(generics.ListCreateAPIView):
    queryset = JobOpening.objects.all()
    serializer_class = JobOpeningSerializer

class JobOpeningDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOpening.objects.all()
    serializer_class = JobOpeningSerializer
