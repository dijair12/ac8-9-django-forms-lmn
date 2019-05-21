from django.test import Client, TestCase
from django.conf import settings
from django.urls import reverse

from cursos.models import Curso

from lmsimpacta.tests import BaseTestCases

class CursoDetalhesTestCase(TestCase):

    def setUp(self):
        self.ads = Curso.objects.create(nome="Análise e Desenvolvimento", sigla='ADS', semestres=4)
        self.cliente = Client()

    def test_responde_url(self):
        response = self.cliente.get('/cursos/ADS/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'curso.html')
        self.assertEqual(response.context["curso"], self.ads)

    def test_responde_urlname(self):
        response = self.cliente.get(reverse("cursos:detalhes", kwargs={'sigla':'ADS'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'curso.html')
        self.assertEqual(response.context["curso"], self.ads)

class CursoInsercaoTestCase(TestCase):

    def setUp(self):
        self.cliente = Client()

    def test_responde_url(self):
        response = self.cliente.get('/cursos/form/novo/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'curso-form.html')

    def test_responde_urlname(self):
        response = self.cliente.get(reverse("cursos:inserir"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'curso-form.html')

    def test_insere_curso(self):
        self.cliente.post('/cursos/form/novo/', {
            'nome': "Sistemas da Informação", 'sigla': 'SI', 'semestres': 8,
        })
        si = Curso.objects.get(sigla="SI")
        self.assertEqual(si.sigla, 'SI')
        self.assertEqual(si.nome, 'Sistemas da Informação')
        self.assertEqual(si.semestres, 8)

class CursoAlteracaoTestCase(TestCase):

    def setUp(self):
        self.bd = Curso.objects.create(nome='Banco de Dados', sigla='BD', semestres=5)
        self.cliente = Client()

    def test_responde_url(self):
        response = self.cliente.get('/cursos/form/BD/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'curso-form.html')
        self.assertEqual(response.context["form"].instance, self.bd)

    def test_responde_urlname(self):
        response = self.cliente.get(reverse('cursos:alterar', kwargs={'sigla': 'BD'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'curso-form.html')
        self.assertEqual(response.context["form"].instance, self.bd)

    def test_altera_curso(self):
        response = self.cliente.post('/cursos/form/BD/', {
            'nome': self.bd.nome, 'sigla': self.bd.sigla, 'semestres': 8
        })
        bd = Curso.objects.get(sigla="BD")
        self.assertEqual(bd.sigla, 'BD')
        self.assertEqual(bd.nome, 'Banco de Dados')
        self.assertEqual(bd.semestres, 8)