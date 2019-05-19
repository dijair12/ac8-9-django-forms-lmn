from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from lmsimpacta.tests import BaseTestCases

class EntrarTestCase(BaseTestCases.SimpleViewTestCase):
    def __init__(self, methodName):
        super().__init__(methodName, '/contas/entrar/', 'contas:entrar', 'login.html')

    def test_static_content(self):
        response = super().test_static_content()
        self.assertContains(response, settings.STATIC_URL+'css/forms.css')
    
    def test_urls_links(self):
        response = super().test_urls_links()
        self.assertContains(response, '"'+reverse('contas:esqueci')+'"')

class EsqueciTestCase(BaseTestCases.SimpleViewTestCase):
    def __init__(self, methodName):
        super().__init__(methodName, '/contas/esqueci-a-senha/', 'contas:esqueci', 'esqueci.html')

    def test_static_content(self):
        response = super().test_static_content()
        self.assertContains(response, settings.STATIC_URL+'css/forms.css')

class InscricaoTestCase(BaseTestCases.SimpleViewTestCase):
    def __init__(self, methodName):
        super().__init__(methodName, '/contas/inscrever/', 'contas:inscrever', 'inscrever.html')

    def test_static_content(self):
        response = super().test_static_content()
        self.assertContains(response, settings.STATIC_URL+'css/forms.css')

class LembrarTestCase(BaseTestCases.SimpleViewTestCase):
    def __init__(self, methodName):
        super().__init__(methodName, '/contas/lembrar/', 'contas:lembrar', 'lembrar.html')
    
    def test_static_content(self):
        response = super().test_static_content()
        self.assertContains(response, settings.STATIC_URL+'css/forms.css')

