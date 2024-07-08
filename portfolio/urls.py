from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('404/', views.error, name='404'),
]
