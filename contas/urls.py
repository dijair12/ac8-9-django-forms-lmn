from django.urls import path

from . import views

contas_urls = ([
    path('entrar/', views.entrar, name='entrar'),
    path('esqueci-a-senha/', views.esqueci, name='esqueci'),
    path('inscrever/', views.inscrever, name='inscrever'),
    path('lembrar/', views.lembrar, name='lembrar')
], 'contas')