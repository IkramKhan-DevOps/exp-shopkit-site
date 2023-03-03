from django.contrib import admin

from .models import (
    DemoRequest, ComplainRequest, Application, ApplicationRegistration
)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'version', 'category', 'operating_system', 'total_downloads', 'created_on', 'is_active']
    list_filter = ['category', 'operating_system']


class DemoRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'time_slot', 'status', 'created_on', 'is_active']
    list_filter = ['status', 'is_active']


class ComplainRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'heading', 'status', 'created_on', 'is_active']
    list_filter = ['status', 'is_active']


class ApplicationRegistrationAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'application', 'software_id', 'is_active', 'created_on'
    ]
    list_filter = ['is_active']


admin.site.register(Application, ApplicationAdmin)
admin.site.register(DemoRequest, DemoRequestAdmin)
admin.site.register(ComplainRequest, ComplainRequestAdmin)
admin.site.register(ApplicationRegistration, ApplicationRegistrationAdmin)


admin.site.site_header = 'ROOT ADMINISTRATION'
admin.site.index_title = 'Swipe X'
admin.site.site_title = 'SSO Dashboard'
