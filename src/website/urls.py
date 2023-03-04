from django.urls import path
from src.website.views import (
    HomeView, DownloadView, download_software, TermsAndConditionsView, PrivacyPolicyView,
    BookADemoView
)

app_name = "website"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('download/', DownloadView.as_view(), name='download'),
    path('book-a-demo/', BookADemoView.as_view(), name='book-a-demo'),
    path('download/application/', download_software, name='download_software'),

    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('terms-and-conditions/', TermsAndConditionsView.as_view(), name='terms-and-conditions'),
]
