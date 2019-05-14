from django.urls import path

from . import views

website_urls = ([
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato')
], 'website')