from django.db import models
from core.base.models import TimeStampedModel


class Location(TimeStampedModel):
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
    name = models.CharField(max_length=255)
    employee_count = models.IntegerField()
    headquarters_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class JobOpening(TimeStampedModel):
    company = models.ForeignKey(Company, related_name='job_openings', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
