from django.test import Client, SimpleTestCase
from django.core import mail

from contas.forms import EntrarForm, EsqueciForm, LembrarForm

class EntrarFormTestCase(SimpleTestCase):

    def test_campos_obrigatorios(self):
        form = EntrarForm({
            "usuario": "",
            "senha": ""
        })
        self.assertFalse(form.is_valid())

        self.assertIn('usuario', form.errors.keys())
        self.assertIn('Este campo é obrigatório.', form.errors["usuario"])
        self.assertIn('senha', form.errors.keys())
        self.assertIn('Este campo é obrigatório.', form.errors["senha"])

    def test_tamanhos_campos(self):
        usuario_grande = "abc"*5
        usuario_pequeno = "abc"
        form = EntrarForm({
            "usuario":usuario_grande
        })
        self.assertFalse(form.is_valid())
        self.assertIn('usuario', form.errors.keys())
        self.assertIn('Certifique-se de que o valor tenha no máximo 10 caracteres (ele possui 15).', form.errors["usuario"])

        form = EntrarForm({
            "usuario":usuario_pequeno
        })
        self.assertFalse(form.is_valid())
        self.assertIn('usuario', form.errors.keys())
        self.assertIn('Certifique-se de que o valor tenha no mínimo 5 caracteres (ele possui 3).', form.errors["usuario"])

        form = EntrarForm({
            "usuario":'abcdef'
        })
        form.is_valid()
        self.assertNotIn('usuario', form.errors.keys())

    def test_autenticar_correto(self):
        form = EntrarForm({
            "usuario": 'user1',
            "senha": "teste1"
        })
        self.assertTrue(form.is_valid())
        self.assertTrue(form.autenticar())
        self.assertEqual(0, len(form.errors))

    def test_autenticar_senha_errada(self):
        form = EntrarForm({
            "usuario": 'user1',
            "senha": "teste2"
        })
        self.assertTrue(form.is_valid())
        self.assertFalse(form.autenticar())
        self.assertEqual(1, len(form.errors))

class EsqueciFormTestCase(SimpleTestCase):

    def test_campos_obrigatorios(self):
        form = EsqueciForm({
            "email": ""
        })
        self.assertFalse(form.is_valid())

        self.assertIn('email', form.errors.keys())
        self.assertIn('Este campo é obrigatório.', form.errors["email"])
        
    def test_email_valido(self):
        form = EsqueciForm({ "email": "seila" })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertIn('Informe um endereço de email válido.', form.errors["email"])

    def test_envia_senha_nao_existe(self):
        form = EsqueciForm({ "email": "naoexiste@email.com" })
        self.assertTrue(form.is_valid())
        form.enviar_senha()
        self.assertIn('email', form.errors.keys())
        self.assertIn('E-mail não cadastrado!', form.errors["email"])

    def test_envia_senha_existe(self):
        form = EsqueciForm({ "email": "user1@email.com" })
        self.assertTrue(form.is_valid())
        form.enviar_senha()
        self.assertNotIn('email', form.errors.keys())
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'FIT Contato - Lembrete de Senha')
        self.assertEqual(mail.outbox[0].to, ['user1@email.com'])
        self.assertEqual(
            mail.outbox[0].body, 
            'A senha do seu usuário é teste1'
        )
        self.assertEqual(mail.outbox[0].from_email, 'contato@fit.com.br')

class LembrarFormTestCase(SimpleTestCase):

    def test_campos_obrigatorios(self):
        form = LembrarForm({
            "senha": "", "confirmar_senha": ""
        })
        self.assertFalse(form.is_valid())
        self.assertIn('senha', form.errors.keys())
        self.assertIn('Este campo é obrigatório.', form.errors["senha"])
        self.assertIn('confirmar_senha', form.errors.keys())
        self.assertIn('Este campo é obrigatório.', form.errors["confirmar_senha"])
        
    def test_salvar_invalido(self):
        form = LembrarForm({
            "senha": "123456", "confirmar_senha": "654321"
        })        
        self.assertTrue(form.is_valid())
        form.salvar_senha()
        self.assertEquals(1, len(form.errors))
        self.assertIn('Senhas devem ser iguais!', form.non_field_errors())

    def test_salvar_valido(self):
        form = LembrarForm({
            "senha": "123456", "confirmar_senha": "123456"
        })        
        self.assertTrue(form.is_valid())
        form.salvar_senha()
        self.assertEquals(0, len(form.errors))