from django.shortcuts import render

def esqueci(request):
    return render(request, 'esqueci.html')

def inscrever(request):
    return render(request, 'inscrever.html')

def entrar(request):
    return render(request, 'login.html')

def lembrar(request):
    return render(request, 'lembrar.html')