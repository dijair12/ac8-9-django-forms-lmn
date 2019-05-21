from django.test import TestCase
from django.db.utils import IntegrityError
from cursos.models import Curso

class CursoModelTest(TestCase):

    def test_nome_not_null(self):
        self.assertRaises(IntegrityError, lambda: Curso.objects.create(nome=None, sigla="ADS", semestres=2))
    
    def test_sigla_not_null(self):
        self.assertRaises(IntegrityError, lambda: Curso.objects.create(nome="nome", sigla=None, semestres=3))

    def test_semestres_not_null(self):
        self.assertRaises(IntegrityError, lambda: Curso.objects.create(nome="nome", sigla="ADS", semestres=None))

    def test_nome_unique(self):
        Curso.objects.create(
            nome="Curso 1",
            sigla="ADS",
            semestres=3,
            coordenador="Takai",
            ementa="Muito conteudo"
        )
        self.assertRaises(IntegrityError, lambda: Curso.objects.create(nome='Curso 1', sigla="SI", semestres=4))

    def test_sigla_unique(self):
        Curso.objects.create(
            nome="Curso 1",
            sigla="ADS",
            semestres=3
        )
        self.assertRaises(IntegrityError, lambda: Curso.objects.create(nome='Curso 4', sigla="ADS", semestres=4))