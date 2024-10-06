from django.contrib import admin
from core.models import JobOpening

@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ['title', 'company_id', 'location_id', 'date_posted']  # Customize list view fields
    search_fields = ['title', 'company__name']  # Allow searching by job title and company name
    list_filter = ['company_id', 'location_id']  # Enable filters by company and location
