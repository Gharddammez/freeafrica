from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
     path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('packages/', views.packages, name='packages'),
    path('destination/', views.destination, name='destination'),
    path('booking/', views.booking, name='booking'),
    path('guides/', views.guides, name='guides'),
    path('testimonial/', views.testimonial, name='testimonial'),
]