# encoding:utf-8
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(
        max_length=150, null=False, blank=False, verbose_name='Cidade')
    uf = models.CharField(max_length=2, null=False, blank=False)
    pais = models.CharField(max_length=50,  null=False, blank=False)

    def __str__(self):
        return self.nome + " - " + self.uf

    class Meta:
        verbose_name = u'Município'
        verbose_name_plural = u'Municípios'
        ordering = ['nome']

    def get_absolute_url(self):
        return reverse('app_enderecos_cidade_update', kwargs={'pk': self.pk})


class Bairro(models.Model):
    nome = models.CharField(
        max_length=150, null=False, blank=False,
        verbose_name='Bairro', help_text='Informe o nome do bairro')
    cidade = models.ForeignKey(Cidade, null=False, blank=False)

    def __str__(self):
        return self.nome + " - " + self.cidade.nome

    def get_absolute_url(self):
        return reverse('app_enderecos_bairro_update', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['nome']


class Endereco(models.Model):
    rua = models.CharField(
        max_length=150, null=False, blank=False, verbose_name=u'Rua / Av.')
    numero = models.IntegerField(null=True, blank=True, default=0)
    bairro = models.ForeignKey(
        Bairro, null=False, blank=False, related_name='bairro')
    cep = models.CharField(max_length=10,   null=False, blank=False)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    rua_comercial = models.CharField(
        max_length=150, null=True, blank=True, verbose_name=u'Rua / Av.')
    numero_comercial = models.IntegerField(
        null=True, blank=True, default=0, verbose_name=u'Nº')
    bairro_comercial = models.ForeignKey(
        Bairro, null=True, blank=True, related_name='bairro_comercial',
        verbose_name=u'Bairro')
    cep_comercial = models.CharField(
        max_length=10,   null=True, blank=True, verbose_name=u'CEP')
    complemento_comercial = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=u'Complemento')

    def __str__(self):
        return u'' + self.rua + u' - ' + self.bairro.nome

    class Meta:
        ordering = ['rua']
