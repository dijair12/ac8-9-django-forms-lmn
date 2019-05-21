from django.test import Client, SimpleTestCase
from django.core import mail

from website.forms import ContatoForm

class ContatoFormTestCase(SimpleTestCase):

    def setUp(self):
        pass


    def test_campos_obrigatorios(self):
        form = ContatoForm({
            "nome": "",
            "assunto": "",
            "mensagem": ""
        })
        self.assertFalse(form.is_valid())

        self.assertIn('nome', form.errors.keys())
        self.assertIn('Este campo é obrigatório.', form.errors["nome"])
        self.assertIn('assunto', form.errors.keys())
        self.assertIn('Este campo é obrigatório.', form.errors["assunto"])
        self.assertIn('mensagem', form.errors.keys())
        self.assertIn('Este campo é obrigatório.', form.errors["mensagem"])

        self.assertNotIn('email', form.errors.keys())
        self.assertNotIn('telefone', form.errors.keys())
        self.assertNotIn('resposta', form.errors.keys())

    def test_tamanhos_campos(self):
        nome_grande = "abc"*50
        form = ContatoForm({
            "nome":nome_grande
        })
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors.keys())
        self.assertIn('Certifique-se de que o valor tenha no máximo 120 caracteres (ele possui 150).', form.errors["nome"])

    def test_email_valido(self):
        form = ContatoForm({ "email": "seila" })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertIn('Informe um endereço de email válido.', form.errors["email"])

    def test_resposta_valido(self):
        form = ContatoForm({ "resposta": ["T"] })
        form.is_valid()
        self.assertNotIn('resposta', form.errors.keys(), msg="T deveria ser uma resposta válida")
        form = ContatoForm({ "resposta": ["E"] })
        form.is_valid()
        self.assertNotIn('resposta', form.errors.keys(), msg="E deveria ser uma resposta válida")
        form = ContatoForm({ "resposta": ["T","E"] })
        form.is_valid()
        self.assertNotIn('resposta', form.errors.keys(), msg="T e E deveriam ser respostas válidas")
        form = ContatoForm({ "resposta": ["X"] })
        form.is_valid()
        self.assertIn('resposta', form.errors.keys(), msg="X não deveria ser uma resposta válida")
        self.assertIn('Faça uma escolha válida. X não é uma das escolhas disponíveis.', form.errors["resposta"])

    def test_assunto_valido(self):
        form = ContatoForm({ "assunto": "B" })
        form.is_valid()
        self.assertNotIn('assunto', form.errors.keys(), msg="B deveria ser um assunto válido")
        form = ContatoForm({ "assunto": "R" })
        form.is_valid()
        self.assertNotIn('assunto', form.errors.keys(), msg="R deveria ser um assunto válido")
        form = ContatoForm({ "assunto": "S" })
        form.is_valid()
        self.assertNotIn('assunto', form.errors.keys(), msg="S deveria ser um assunto válido")
        form = ContatoForm({ "assunto": "Z" })
        form.is_valid()
        self.assertIn('assunto', form.errors.keys(), msg="Z não deveria ser um assunto válido")
        self.assertIn('Faça uma escolha válida. Z não é uma das escolhas disponíveis.', form.errors["assunto"])

    def test_reposta_contato(self):
        form = ContatoForm({ "resposta": ["T"], "telefone": "" })
        self.assertFalse(form.is_valid())
        self.assertIn('telefone', form.errors.keys())
        self.assertIn('Telefone é obrigatório quando for escolhido como resposta.', form.errors["telefone"])
        
        form = ContatoForm({ "resposta": ["E"], "email": "" })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertIn('E-mail é obrigatório quando for escolhido como resposta.', form.errors["email"])

    def test_envia_email(self):
        dados = {
            'nome': 'José da Silva',
            'email': 'email@gmail.com',
            'telefone': '(11) 99999-9999',
            'mensagem': 'Olá FIT!',
            'resposta': ['T','E'],
            'assunto': 'B'
        }
        form = ContatoForm(dados)
        self.assertTrue(form.is_valid())
        form.enviar_email()
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
