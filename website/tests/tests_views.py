from django.conf import settings
from django.core import mail
from django.test import Client, SimpleTestCase
from django.urls import reverse

from lmsimpacta.tests import BaseTestCases

class HomeTestCase(BaseTestCases.SimpleViewTestCase):
    def __init__(self, methodName):
        super().__init__(methodName, '/', 'website:home', 'index.html')
    
    def test_static_content(self):
        response = super().test_static_content()
        self.assertContains(response, settings.STATIC_URL+'css/index.css')
        self.assertContains(response, settings.STATIC_URL+'imagens/enade-ADM.png')
        self.assertContains(response, settings.STATIC_URL+'imagens/enade-ADS.png')
        self.assertContains(response, settings.STATIC_URL+'imagens/enade-RD.png')
        self.assertContains(response, settings.STATIC_URL+'imagens/enade-SI.png')
        self.assertContains(response, settings.STATIC_URL+'imagens/play-smartclass.jpg')

class ContatoTestCase(BaseTestCases.SimpleViewTestCase):
    def __init__(self, methodName):
        super().__init__(methodName, '/contato/', 'website:contato', 'contato.html')

    def test_send_mail(self):
        message = {
            'nome': 'José da Silva',
            'email': 'email@gmail.com',
            'telefone': '(11) 99999-9999',
            'mensagem': 'Olá FIT!',
            'resposta': ['T','E'],
            'assunto': 'B'
        }
        self.client.post(self.url, message)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'FIT Contato - Bug')
        self.assertEqual(mail.outbox[0].to, ['contato@fit.com.br'])
        self.assertEqual(
            mail.outbox[0].body, 
            'Você recebeu o contato do seguinte usuário:\n' \
            '->Nome: José da Silva\n' \
            '->E-mail: email@gmail.com\n' \
            '->Telefone: (11) 99999-9999\n' \
            '->Assunto: Bug\n' \
            '->Resposta: Telefone;E-mail;\n' \
            '->Mensagem: Olá FIT!'
        )
        self.assertEqual(mail.outbox[0].from_email, 'email@gmail.com')

    def test_static_content(self):
        response = super().test_static_content()
        self.assertContains(response, settings.STATIC_URL+'css/forms.css')
