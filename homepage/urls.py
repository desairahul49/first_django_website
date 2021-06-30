from django.contrib import admin
from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('solutions', views.solutions, name='solutions'),
    path('contact', views.contact, name='contact'),
]