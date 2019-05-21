from django import forms
from django.core.mail import send_mail
from .data import USUARIOS

class EntrarForm(forms.Form):

    def autenticar(self):
        pass

class EsqueciForm(forms.Form):

    def enviar_senha(self):
        pass

class LembrarForm(forms.Form):

    senha = forms.CharField()
    confirmar_senha = forms.CharField()

    def salvar_senha(self):
        senha = self.cleaned_data.get("senha")
        senha2 = self.cleaned_data.get("confirmar_senha")

        if senha != senha2:
            self.add_error(None, "Senhas devem ser iguais!")