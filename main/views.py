from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def pricing(request):
    return render(request, 'pricing.html')


def contact(request):
    return render(request, 'contact.html')


def quote(request):
    return render(request, 'get-a-quote.html')


def terms_of_service(request):
    return None


def privacy_policy(request):
    return None


def service_details(request):
    return render(request, 'service-details.html')