# encoding:utf-8
from django.db import models
from enderecos.models import Endereco


class Empresa(models.Model):
    nome = models.CharField(
        max_length=150, null=False,
        blank=False, verbose_name=u"Nome da Empresa")
    cnpj = models.CharField(
        max_length=150, null=False, blank=False,
        verbose_name=u'CNPJ da Empresa')
    logo = models.ImageField(
        upload_to='Logo', max_length=100)

    ativo = models.NullBooleanField(null=False, blank=False, default=True)
    endereco = models.ForeignKey(Endereco)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
