
from django import forms
from django.forms import ModelForm, ValidationError
from .models import *

class MensagemForm(forms.ModelForm):
    
    class Meta:
        model = Messagem
        widgets = {'user': forms.HiddenInput(), 'sala': forms.HiddenInput()}
        exclude = []
