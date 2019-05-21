from django import forms
from django.core.mail import send_mail

class ContatoForm(forms.Form):

    def enviar_email(self):
        pass