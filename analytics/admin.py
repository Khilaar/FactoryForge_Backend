from django.contrib import admin
from .models import Analytics

class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'user', 'description')
    search_fields = ('date', 'user')

# Register the Analytics model with its admin class
admin.site.register(Analytics, AnalyticsAdmin)