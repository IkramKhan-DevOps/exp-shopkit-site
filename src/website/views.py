from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'website/index.html'


class DownloadView(TemplateView):
    template_name = 'website/downloads.html'
