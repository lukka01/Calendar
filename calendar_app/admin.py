from django.contrib import admin

from django.contrib import admin
from .models import Calendar

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('year', 'month', 'day', 'created_at')
    list_filter = ('year', 'month')
