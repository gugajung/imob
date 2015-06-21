# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table(u'clientes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('cnpj_cpf', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('rg', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('orgao_expeditor', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('nome_pai', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nome_mae', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nacionalidade', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('naturalidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['enderecos.Cidade'])),
            ('endereco', self.gf('django.db.models.fields.related.ForeignKey')(related_name='endereco_cli', to=orm['enderecos.Endereco'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'], null=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('data_cadastro', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True)),
            ('data_nascimento', self.gf('django.db.models.fields.DateField')()),
            ('telefone_fixo', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('telefone_comercial', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('celular_2', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('tipo_cliente', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('estado_civil', self.gf('django.db.models.fields.CharField')(default='S', max_length=1)),
            ('tipo_pessoa', self.gf('django.db.models.fields.CharField')(default='F', max_length=1)),
            ('profissao', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('empresa_trabalha', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('renda', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('conjuge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'], null=True, blank=True)),
            ('referencias_bancarias', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('referencias_comerciais', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('referencias_pessoais', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['Cliente'])


    def backwards(self, orm):
        # Deleting model 'Cliente'
        db.delete_table(u'clientes_cliente')


    models = {
        u'clientes.cliente': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Cliente'},
            'ativo': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'celular_2': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'cnpj_cpf': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'conjuge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']", 'null': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']", 'null': 'True', 'blank': 'True'}),
            'empresa_trabalha': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'endereco_cli'", 'to': u"orm['enderecos.Endereco']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacionalidade': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'naturalidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Cidade']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nome_mae': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nome_pai': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'observacoes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'orgao_expeditor': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'profissao': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'referencias_bancarias': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'referencias_comerciais': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'referencias_pessoais': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'renda': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'telefone_comercial': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'telefone_fixo': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'tipo_cliente': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'tipo_pessoa': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'})
        },
        u'empresas.empresa': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Empresa'},
            'ativo': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Endereco']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'enderecos.bairro': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Bairro'},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Cidade']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'enderecos.cidade': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Cidade'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'enderecos.endereco': {
            'Meta': {'ordering': "['rua']", 'object_name': 'Endereco'},
            'bairro': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bairro'", 'to': u"orm['enderecos.Bairro']"}),
            'bairro_comercial': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bairro_comercial'", 'null': 'True', 'to': u"orm['enderecos.Bairro']"}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'cep_comercial': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'complemento_comercial': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'numero_comercial': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'rua': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'rua_comercial': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['clientes']