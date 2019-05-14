from django.urls import path

from . import views

restrito_urls = ([
    path('notas/', views.notas, name='notas')
], 'restrito')