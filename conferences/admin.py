from django.contrib import admin
from .models import Conference

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['name', 'acronym', 'submission_deadline']
    list_filter = ['submission_deadline']
    search_fields = ['name', 'acronym', 'description']