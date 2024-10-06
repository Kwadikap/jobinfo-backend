from rest_framework import serializers
from core.models import JobOpening

class JobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpening
        fields = '__all__'
