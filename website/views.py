from django.core.mail import send_mail
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def contato(request):
    if request.POST:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        mensagem = request.POST.get('mensagem')
        
        assunto = request.POST.get('assunto')
        if assunto == 'R':
            assunto = 'Reclamação'
        elif assunto == 'S':
            assunto = 'Sugestão'
        else:
            assunto = 'Bug'
        assunto_email = 'FIT Contato - '+assunto

        resposta = request.POST.getlist('resposta')
        resposta_email = ''
        for resp in resposta:
            resposta_email += 'E-mail;' if resp == 'E' else 'Telefone;'

        mensagem_email = 'Você recebeu o contato do seguinte usuário:\n'\
            '->Nome: '+nome+'\n'\
            '->E-mail: '+email+'\n'\
            '->Telefone: '+telefone+'\n'\
            '->Assunto: '+assunto +'\n'\
            '->Resposta: '+resposta_email+'\n'\
            '->Mensagem: '+mensagem

        send_mail(
            assunto_email,
            mensagem_email,
            email,
            ['contato@fit.com.br']
        )

    return render(request, 'contato.html')