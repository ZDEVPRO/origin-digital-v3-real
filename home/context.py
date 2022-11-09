from home.models import SiteLogo


def site_logo_view(request):
    logo_site = SiteLogo.objects.all().order_by('-id')[:1]

    context = {
        'logo_site': logo_site
    }
    return context
