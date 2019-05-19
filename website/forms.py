from django import forms
from django.core.mail import send_mail

class ContatoForm(forms.Form):
    
    # Campos do formulário

    def enviar_email(self):
        pass