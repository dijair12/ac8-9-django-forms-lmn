from django.urls import path

from . import views

RESTRITO_URLS = ([
    path('notas/', views.notas, name='notas')
], 'restrito')