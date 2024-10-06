from django.contrib import admin
from core.models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'state', 'country', 'zip_code']  # Customize which fields are shown in the admin list view
    search_fields = ['city', 'state', 'country', 'zip_code']  # Enable search functionality for these fields
    list_filter = ['country', 'state']  # Add filters for the country and state fields
