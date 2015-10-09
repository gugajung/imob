# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cidade'
        db.create_table(u'enderecos_cidade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('uf', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'enderecos', ['Cidade'])

        # Adding model 'Bairro'
        db.create_table(u'enderecos_bairro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('cidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['enderecos.Cidade'])),
        ))
        db.send_create_signal(u'enderecos', ['Bairro'])

        # Adding model 'Endereco'
        db.create_table(u'enderecos_endereco', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rua', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('bairro', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bairro', to=orm['enderecos.Bairro'])),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('complemento', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('rua_comercial', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('numero_comercial', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('bairro_comercial', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='bairro_comercial', null=True, to=orm['enderecos.Bairro'])),
            ('cep_comercial', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('complemento_comercial', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'enderecos', ['Endereco'])


    def backwards(self, orm):
        # Deleting model 'Cidade'
        db.delete_table(u'enderecos_cidade')

        # Deleting model 'Bairro'
        db.delete_table(u'enderecos_bairro')

        # Deleting model 'Endereco'
        db.delete_table(u'enderecos_endereco')


    models = {
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

    complete_apps = ['enderecos']