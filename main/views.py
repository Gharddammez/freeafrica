from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def destination(request):
    return render(request, 'destination.html')


def booking(request):
    return render(request, 'booking.html')


def guides(request):
    return render(request, 'guides.html')


def testimonial(request):
    return render(request, 'testimonial.html')

def packages(request):
    return render(request, 'packages.html')

def contact(request):
    return render(request, 'contact.html')