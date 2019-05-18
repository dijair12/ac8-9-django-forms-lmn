from django.test import TestCase
from django.conf import settings

from lmsimpacta.tests import BaseTestCases

class NotasTestCase(BaseTestCases.SimpleViewTestCase):
    def __init__(self, methodName):
        super().__init__(methodName, '/restrito/notas/', 'restrito:notas', 'notas.html')
    
    def test_static_content(self):
        response = super().test_static_content()
        self.assertContains(response, settings.STATIC_URL+'css/notas.css')
        self.assertContains(response, settings.STATIC_URL+'scripts/notas.js')
