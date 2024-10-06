from django.db import models
from core.base.models import TimeStampedModel
import uuid


class Location(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20, null=True, blank=True)

    @property
    def complete_address(self) -> str:
        """Return the full location as a formatted string."""
        address_parts = [self.city, self.state, self.zip_code, self.country]
        return ', '.join([part for part in address_parts if part])
    
    def __str__(self) -> str:
        return self.complete_address


class Company(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    employee_count = models.IntegerField()
    headquarters_location_id = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class JobOpening(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.ForeignKey(Company, related_name='job_openings', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location_id = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
