from django import forms
from parametros.models import ParametrosGerais


class FormParametrosGerais(forms.ModelForm):
    class Meta:
        model = ParametrosGerais
        exclude = ['*']
