from django.urls import path, re_path
from django.views.static import serve

from core import settings
from src.website.views import HomeView, DownloadView, download_software

app_name = "website"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('download/', DownloadView.as_view(), name='download'),
    path('download/application/', download_software, name='download_software'),
]
