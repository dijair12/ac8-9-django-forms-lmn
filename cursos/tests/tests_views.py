from django.test import TestCase

from django.test import TestCase
from django.conf import settings

from lmsimpacta.tests import BaseTestCases

class AdsTestCase(BaseTestCases.SimpleViewTestCase):
    def __init__(self, methodName):
        super().__init__(methodName, '/cursos/ads/', 'cursos:ads', 'ads.html')
    
    def test_static_content(self):
        response = super().test_static_content()
        self.assertContains(response, settings.STATIC_URL+'css/cursos.css')

class SiTestCase(BaseTestCases.SimpleViewTestCase):
    def __init__(self, methodName):
        super().__init__(methodName, '/cursos/si/', 'cursos:si', 'si.html')
    
    def test_static_content(self):
        response = super().test_static_content()
        self.assertContains(response, settings.STATIC_URL+'css/cursos.css')

class GtiTestCase(BaseTestCases.SimpleViewTestCase):
    def __init__(self, methodName):
        super().__init__(methodName, '/cursos/gti/', 'cursos:gti', 'gti.html')
    
    def test_static_content(self):
        response = super().test_static_content()
        self.assertContains(response, settings.STATIC_URL+'css/cursos.css')

class BdTestCase(BaseTestCases.SimpleViewTestCase):
    def __init__(self, methodName):
        super().__init__(methodName, '/cursos/bd/', 'cursos:bd', 'bd.html')
    
    def test_static_content(self):
        response = super().test_static_content()
        self.assertContains(response, settings.STATIC_URL+'css/cursos.css')
