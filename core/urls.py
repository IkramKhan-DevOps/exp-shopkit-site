from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from core.settings import ENVIRONMENT


def handler404(request, *args, **kwargs):
    return render(request, "404.html")


def handler500(request, *args, **kwargs):
    return render(request, "500.html")


urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    path('', include('src.website.urls', namespace='website')),
]


if ENVIRONMENT != 'server':
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls"))
    ]
