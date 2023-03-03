from django.http import Http404, FileResponse
from django.views.generic import TemplateView

from src.administration.admins.models import Application


class HomeView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


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


class PrivacyPolicyView(TemplateView):
    template_name = 'website/privacy-policy.html'


class TermsAndConditionsView(TemplateView):
    template_name = 'website/terms-and-conditions.html'


def download_software(request):

    operation_system = request.GET.get('os')
    category = request.GET.get('category')

    # IF category and os available and if parameters are correct.
    if operation_system and category and category in ['p', 'f'] and operation_system in ['w', 'g', 'm', 'l']:

        # CHECK: if requested version is available or not
        app = Application.objects.filter(category=category, operating_system=operation_system).order_by('-version')
        if app:

            # STATISTICS: update statistics
            app = app[0]
            app.total_downloads += 1
            app.save()

            # SAVE: download settings
            file = app.app_file
            file_extension = str(file).split('.')[1]
            file_name = f"{app.name}-{app.get_category_display()} v{app.version} for {app.get_operating_system_display()}.{file_extension}"
            response = FileResponse(file)
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response

    raise Http404
