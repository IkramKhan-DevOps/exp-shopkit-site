from django.urls import path
from src.website.views import HomeView, DownloadView

app_name = "website"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('download/', DownloadView.as_view(), name='download'),
]
