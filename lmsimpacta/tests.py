from django.conf import settings
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage
from django.test import TestCase
from django.urls import reverse


class BaseTestCases:

    class SimpleViewTestCase(TestCase):

        def __init__(self, methodName, url=None, url_name=None, template_name=None):
            super().__init__(methodName)
            self.url = url
            self.url_name = url_name
            self.template_name = template_name

        def setUp(self):
            self.client = self.client_class()

        def test_urls_links(self):
            response = self.client.get(self.url)
            self.assertContains(response, '"'+reverse('website:home')+'"')
            self.assertContains(response, '"'+reverse('website:contato')+'"')
            self.assertContains(response, '"'+reverse('contas:inscrever')+'"')
            self.assertContains(response, '"'+reverse('contas:entrar')+'"')
            self.assertContains(response, '"'+reverse('cursos:bd')+'"')
            self.assertContains(response, '"'+reverse('cursos:gti')+'"')
            self.assertContains(response, '"'+reverse('cursos:ads')+'"')
            self.assertContains(response, '"'+reverse('cursos:si')+'"')
            return response

        def test_static_content(self):
            response = self.client.get(self.url)
            self.assertContains(response, settings.STATIC_URL+'css/site.css')
            self.assertContains(response, settings.STATIC_URL+'favicon.ico')
            self.assertContains(response, settings.STATIC_URL+'imagens/impacta-logo.png')
            return response

        def test_url_ok(self):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)

        def test_url_name_ok(self):
            response = self.client.get(reverse(self.url_name))
            self.assertEqual(response.status_code, 200)

        def test_template_ok(self):
            response = self.client.get(self.url)
            self.assertTemplateUsed(response, 'base.html')
            self.assertTemplateUsed(response, self.template_name)

class LmsImpactaTestCase(TestCase):

    def setUp(self):
        pass
    
    
    def validar_app(self, app_name):
        try:
            app_name_verbose = app_name[0].upper()+app_name[1:]
            from website.apps import WebsiteConfig
            self.assertTrue(
                app_name in settings.INSTALLED_APPS or app_name+'.apps.'+app_name_verbose+'Config' in settings.INSTALLED_APPS,
                'Aplicação existe, mas não foi corretamente instalada'
            )
        except ImportError:
            self.fail('Não foi encontrada a aplicação {} (ou o arquivo apps dentro)'.format(app_name))        


    def test_app_restrito(self):
        self.validar_app('restrito')

    def test_app_contas(self):
        self.validar_app('contas')

    def test_app_cursos(self):
        self.validar_app('cursos')

    def test_app_website(self):
        self.validar_app('website')