from django.contrib import admin
from core.models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'headquarters_location_id']  # Example customization for the Company model admin interface
