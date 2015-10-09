from django.contrib import admin
from enderecos.models import Endereco, Bairro, Cidade

admin.site.register(Cidade)
admin.site.register(Endereco)
admin.site.register(Bairro)
