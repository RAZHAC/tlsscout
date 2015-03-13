from django.shortcuts import render
from django.conf import settings

def dashboard(request):
    if request.user.is_authenticated():
        ### show dashboard
        return render(request, 'dashboard/dashboard.html')
    else:
        ### show frontpage with brief teaser and login box
        return render(request, 'dashboard/frontpage.html', {
            'SSLLABS_SCANNERURL': settings.SSLLABS_SCANNERURL,
            'SSLLABS_TERMSURL': settings.SSLLABS_TERMSURL,
        })
