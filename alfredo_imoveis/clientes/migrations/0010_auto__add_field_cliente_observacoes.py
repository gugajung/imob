# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cliente.observacoes'
        db.add_column(u'clientes_cliente', 'observacoes',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cliente.observacoes'
        db.delete_column(u'clientes_cliente', 'observacoes')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'ativo': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'celular_2': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'cnpj_cpf': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'conjuge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']", 'null': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']", 'null': 'True', 'blank': 'True'}),
            'empresa_socio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'empresa_trabalha': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'end_empresa_socio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'endereco_cli'", 'to': u"orm['enderecos.Endereco']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacionalidade': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'naturalidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Cidade']", 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nome_mae': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nome_pai': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'observacoes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'orgao_expeditor': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'profissao': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'referencias_bancarias': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'referencias_comerciais': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'renda': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'socio_empresa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telefone_comercial': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'telefone_fixo': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'tipo_cliente': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'})
        },
        u'empresas.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'ativo': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'enderecos.bairro': {
            'Meta': {'object_name': 'Bairro'},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Cidade']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'enderecos.cidade': {
            'Meta': {'object_name': 'Cidade'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'enderecos.endereco': {
            'Meta': {'object_name': 'Endereco'},
            'bairro': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bairro'", 'null': 'True', 'to': u"orm['enderecos.Bairro']"}),
            'bairro_comercial': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bairro_comercial'", 'null': 'True', 'to': u"orm['enderecos.Bairro']"}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'cep_comercial': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'complemento_comercial': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'numero_comercial': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'rua': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'rua_comercial': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['clientes']