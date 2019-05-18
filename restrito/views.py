from django.shortcuts import render

def notas(request):
    return render(request, 'notas.html')