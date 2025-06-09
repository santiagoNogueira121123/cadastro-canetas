from django import forms
from .models import Caneta

class CanetaForm(forms.ModelForm):
    class Meta:
        model = Caneta
        fields = ['marca','cor','preco']
       
