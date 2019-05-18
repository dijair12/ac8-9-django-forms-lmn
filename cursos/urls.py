from django.urls import path

from . import views

CURSOS_URLS = ([
    path('ads/', views.ads, name='ads'),
    path('bd/', views.bd, name='bd'),
    path('gti/', views.gti, name='gti'),
    path('si/', views.si, name='si'),
], 'cursos')