from django.shortcuts import render
from django.http import HttpResponse

def app_ads_txt(request):
    with open('mysite/web/app-ads.txt', 'r') as f:
        content = f.read()
    return HttpResponse(content, content_type='text/plain')

def index(request):
    """Página de inicio con temática de juego."""
    return render(request, 'helfy/index.html')

def privacy_policy(request):
    """Política de Privacidad - Enfoque 'No Data Collection'."""
    return render(request, 'helfy/privacy.html')

def terms_of_service(request):
    """Términos de Uso - Centrado en uso de la App y anuncios."""
    return render(request, 'helfy/terms.html')