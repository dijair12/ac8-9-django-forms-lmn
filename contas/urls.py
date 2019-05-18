from django.urls import path

from . import views

CONTAS_URLS = ([
    path('entrar/', views.entrar, name='entrar'),
    path('inscrever/', views.inscrever, name='inscrever'),
    path('lembrar/', views.lembrar, name='lembrar'),
    path('esqueci-a-senha/', views.esqueci, name='esqueci'),
], 'contas')