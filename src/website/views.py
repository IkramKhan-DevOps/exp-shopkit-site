import os

from django.http import HttpResponse, Http404, FileResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from core import settings
from src.website.models import Application


class HomeView(TemplateView):
    template_name = 'website/index.html'


class DownloadView(TemplateView):
    template_name = 'website/downloads.html'

    def get_context_data(self, **kwargs):
        context = super(DownloadView, self).get_context_data(**kwargs)

        windows_app_free = Application.objects.filter(operating_system='w', category='f').order_by('-version')
        global_app_free = Application.objects.filter(operating_system='g', category='f').order_by('-version')
        linux_app_free = Application.objects.filter(operating_system='l', category='f').order_by('-version')
        mac_app_free = Application.objects.filter(operating_system='m', category='f').order_by('-version')

        windows_app_premium = Application.objects.filter(operating_system='w', category='p').order_by('-version')
        global_app_premium = Application.objects.filter(operating_system='g', category='p').order_by('-version')
        linux_app_premium = Application.objects.filter(operating_system='l', category='p').order_by('-version')
        mac_app_premium = Application.objects.filter(operating_system='m', category='p').order_by('-version')

        context['windows_app_free'] = windows_app_free.first() if windows_app_free else None
        context['linux_app_free'] = linux_app_free.first() if linux_app_free else None
        context['global_app_free'] = global_app_free.first() if global_app_free else None
        context['mac_app_free'] = mac_app_free.first() if mac_app_free else None

        context['windows_app_premium'] = windows_app_premium.first() if windows_app_premium else None
        context['linux_app_premium'] = linux_app_premium.first() if linux_app_premium else None
        context['global_app_premium'] = global_app_premium.first() if global_app_premium else None
        context['mac_app_premium'] = mac_app_premium.first() if mac_app_premium else None

        return context


def download_software(request):
    file = open('media/PodTalk-1.0.0.zip', 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename="software.exe"'
    return response
