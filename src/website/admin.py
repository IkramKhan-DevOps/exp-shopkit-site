from django.contrib import admin
from .models import Application, TutorialVideo


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'version', 'category', 'operating_system', 'total_downloads', 'created_on', 'is_active']
    list_filter = ['category', 'operating_system']


class TutorialVideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'video_type', 'created_on', 'is_active']
    list_filter = ['video_type']


admin.site.register(Application, ApplicationAdmin)
admin.site.register(TutorialVideo, TutorialVideoAdmin)

admin.site.site_header = 'ROOT ADMINISTRATION'
admin.site.index_title = 'SHOP KIT'
admin.site.site_title = 'root administration'
