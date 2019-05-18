from django.urls import path

from . import views

WEBSITE_URLS = ([
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato')
], 'website')