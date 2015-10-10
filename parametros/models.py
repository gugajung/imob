# encoding:utf8
from django.db import models
from django.contrib.auth.models import User
from financeiro.models.conta_caixa import ContaCaixa


class ParametrosGerais(models.Model):
    taxa_juros = models.DecimalField(max_digits=4, decimal_places=2)
    multa = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    texto_carta_aniv1 = models.TextField('Texto da carta de aniversário 1')
    texto_carta_aniv2 = models.TextField('Texto da carta de aniversário 2')
    texto_carta_aniv3 = models.TextField('Texto da carta de aniversário 3')
    clausula_contrato_adic = models.TextField('Cláusula de contrato adicional')
    gerente = models.ForeignKey(User, verbose_name="Usuário gerente",
                                help_text="Informe o gerente da empresa")
    conta_caixa = models.ForeignKey(
        ContaCaixa, null=True, blank=True,
        verbose_name='Conta caixa para financeiro de contratos')

    def __str__(self):
        return str(self.id) + " - " + u"Parâmetros "
