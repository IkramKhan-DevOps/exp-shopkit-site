from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'version', 'category', 'operating_system', 'created_on', 'updated_on', 'is_active']
    list_filter = ['category', 'operating_system']


admin.site.register(Application, ApplicationAdmin)
