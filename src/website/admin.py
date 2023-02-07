from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'version', 'category', 'operating_system', 'total_downloads', 'created_on', 'is_active']
    list_filter = ['category', 'operating_system']


admin.site.register(Application, ApplicationAdmin)

admin.site.site_header = 'ROOT ADMINISTRATION'
admin.site.index_title = 'SHOP KIT'
admin.site.site_title = 'root administration'
