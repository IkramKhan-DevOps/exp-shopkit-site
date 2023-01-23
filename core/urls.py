
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from core.settings import ENVIRONMENT

urlpatterns = [
    path('admin/', admin.site.urls),
]

# your apps urls
urlpatterns += [
    path('', include('src.website.urls', namespace='website')),
]

if ENVIRONMENT != 'server':
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls"))
    ]
