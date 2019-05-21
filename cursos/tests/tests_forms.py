from django.test import TestCase

from cursos.forms import CursoForm

class CursoFormTestCase(TestCase):

    def test_campos_obrigatorios(self):
        form = CursoForm({
            "nome": "",
            "sigla": "",
            "semestres": ""
        })
        self.assertFalse(form.is_valid())

        self.assertIn('nome', form.errors.keys())
        self.assertIn('Este campo é obrigatório.', form.errors["nome"])
        self.assertIn('sigla', form.errors.keys())
        self.assertIn('Este campo é obrigatório.', form.errors["sigla"])
        self.assertIn('semestres', form.errors.keys())
        self.assertIn('Este campo é obrigatório.', form.errors["semestres"])

    def test_tamanhos_campos(self):
        nome_grande = "abc"*53
        form = CursoForm({
            "nome":nome_grande,
            "sigla": "abcdefg",
            "coordenador": "abcdef" * 21
        })
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors.keys())
        self.assertIn('Certifique-se de que o valor tenha no máximo 100 caracteres (ele possui 159).', form.errors["nome"])
        self.assertIn('sigla', form.errors.keys())
        self.assertIn('Certifique-se de que o valor tenha no máximo 5 caracteres (ele possui 7).', form.errors["sigla"])
        self.assertIn('coordenador', form.errors.keys())
        self.assertIn('Certifique-se de que o valor tenha no máximo 120 caracteres (ele possui 126).', form.errors["coordenador"])

    def test_save_ok(self):
        curso_dados = {
            "nome":"Curso 1",
            "sigla": "ADS",
            "semestres": 4,
            "coordenador": "Takai",
            "ementa": "Muito conteúdo"
        }
        form = CursoForm(curso_dados)
        self.assertTrue(form.is_valid())
        curso = form.save()
        self.assertEqual(curso.nome, curso_dados["nome"])
        self.assertEqual(curso.sigla, curso_dados["sigla"])
        self.assertEqual(curso.semestres, curso_dados["semestres"])
        self.assertEqual(curso.coordenador, curso_dados["coordenador"])
        self.assertEqual(curso.ementa, curso_dados["ementa"])
