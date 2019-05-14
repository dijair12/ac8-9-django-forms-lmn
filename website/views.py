from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'index.html')

def contato(request):
    if request.POST:
        email_origem = request.POST.get('email', '')
        email_destino = 'contato@fit.com.br'
        nome = request.POST.get('nome', '')
        telefone = request.POST.get('telefone', '')
        
        resposta = request.POST.getlist('resposta')
        resposta_msg = ''
        for resp in resposta:
            if resp == 'T':
                resposta_msg += 'Telefone;'
            else:
                resposta_msg += 'E-mail;'

        assunto = request.POST.get('assunto', '')
        if assunto == 'B':
            assunto = 'Bug'
        elif assunto == 'R':
            assunto = 'Reclamação'
        else:
            assunto = 'Sugestão'
        assunto_mensagem = 'FIT Contato - '+assunto

        mensagem = request.POST.get('mensagem', '')
        mensagem = 'Você recebeu o contato do seguinte usuário:\n' \
            '->Nome: ' + nome + '\n' \
            '->E-mail: ' + email_origem + '\n' \
            '->Telefone: ' + telefone + '\n' \
            '->Assunto: ' + assunto + '\n' \
            '->Resposta: ' + resposta_msg + '\n' \
            '->Mensagem: ' + mensagem

        send_mail(
            assunto_mensagem,
            mensagem, 
            email_origem,
            [email_destino]
        )

    return render(request, 'contato.html')