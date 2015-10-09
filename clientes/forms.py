from django import forms
from clientes.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['endereco', 'endereco_comercial']
        read_only = ['data_cadastro']


class ClienteFormVisualizar(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['endereco', 'endereco_comercial']
        read_only = ['*']
