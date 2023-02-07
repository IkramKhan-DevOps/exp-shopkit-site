from django.urls import path
from src.website.views import HomeView, DownloadView, download_software, TermsAndConditionsView, PrivacyPolicyView

app_name = "website"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('download/', DownloadView.as_view(), name='download'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='download'),
    path('terms-and-conditions/', TermsAndConditionsView.as_view(), name='download'),
    path('download/', DownloadView.as_view(), name='download'),
    path('download/application/', download_software, name='download_software'),
]
