# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContaCaixa'
        db.create_table(u'financeiro_contacaixa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('conta_caixa_superior', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financeiro.ContaCaixa'], null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
        ))
        db.send_create_signal('financeiro', ['ContaCaixa'])

        # Adding model 'Titulo'
        db.create_table(u'financeiro_titulo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('conta_caixa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financeiro.ContaCaixa'], null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
            ('data_cadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('vencimento', self.gf('django.db.models.fields.DateField')()),
            ('data_quitacao', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('usuario_cadastrou', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('valor_copasa', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=6, decimal_places=2, blank=True)),
            ('valor_cemig', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=6, decimal_places=2, blank=True)),
            ('valor_encargos', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=6, decimal_places=2, blank=True)),
            ('perc_juros', self.gf('django.db.models.fields.DecimalField')(default=0.0, null=True, max_digits=4, decimal_places=2, blank=True)),
            ('taxa_multa', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('valor_iptu_pago', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('pagamento_parcial', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=6, decimal_places=2, blank=True)),
            ('deletado', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'], null=True)),
            ('contrato_locacao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imoveis.ContratoLocacao'], null=True, blank=True)),
            ('valor_condominio_pago', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('conta_parcelas', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descricao_encargos', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('financeiro', ['Titulo'])

        # Adding model 'Recibo'
        db.create_table(u'financeiro_recibo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financeiro.Titulo'])),
            ('data_cadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('financeiro', ['Recibo'])


    def backwards(self, orm):
        # Deleting model 'ContaCaixa'
        db.delete_table(u'financeiro_contacaixa')

        # Deleting model 'Titulo'
        db.delete_table(u'financeiro_titulo')

        # Deleting model 'Recibo'
        db.delete_table(u'financeiro_recibo')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        },
        'financeiro.contacaixa': {
            'Meta': {'ordering': "['descricao']", 'object_name': 'ContaCaixa'},
            'conta_caixa_superior': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financeiro.ContaCaixa']", 'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'financeiro.recibo': {
            'Meta': {'object_name': 'Recibo'},
            'data_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financeiro.Titulo']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'financeiro.titulo': {
            'Meta': {'ordering': "['descricao']", 'object_name': 'Titulo'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']", 'null': 'True'}),
            'conta_caixa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financeiro.ContaCaixa']", 'null': 'True', 'blank': 'True'}),
            'conta_parcelas': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'contrato_locacao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['imoveis.ContratoLocacao']", 'null': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_quitacao': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'deletado': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'descricao_encargos': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacoes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagamento_parcial': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'perc_juros': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'taxa_multa': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'usuario_cadastrou': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'valor_cemig': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'valor_condominio_pago': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'valor_copasa': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'valor_encargos': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'valor_iptu_pago': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'vencimento': ('django.db.models.fields.DateField', [], {})
        },
        u'imoveis.contratolocacao': {
            'Meta': {'object_name': 'ContratoLocacao'},
            'data_emissao_contrato': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            'fiador1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fiador1_contrato'", 'to': u"orm['clientes.Cliente']"}),
            'fiador2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fiador2_contrato'", 'null': 'True', 'to': u"orm['clientes.Cliente']"}),
            'fiador3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fiador3_contrato'", 'null': 'True', 'to': u"orm['clientes.Cliente']"}),
            'gerou_receber': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imovel': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['imoveis.Imovel']", 'unique': 'True'}),
            'inicio_contrato': ('django.db.models.fields.DateField', [], {}),
            'locatario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locatario_contrato'", 'to': u"orm['clientes.Cliente']"}),
            'observacao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'termino_contrato': ('django.db.models.fields.DateField', [], {}),
            'tipo_contrato': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'imoveis.imovel': {
            'Meta': {'ordering': "['descricao']", 'object_name': 'Imovel'},
            'area_construida': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'area_lote': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cod_ref_site': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_last_pag_iptu': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Endereco']"}),
            'horario_visitas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_chaves': ('django.db.models.fields.CharField', [], {'default': "'I'", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'pavimentos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'proprietario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'tipo_imovel': ('django.db.models.fields.CharField', [], {'default': "'R'", 'max_length': '1'}),
            'ultima_vistoria': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'valor_aluguel': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'valor_condominio': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'valor_iptu': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'vencimento_iptu': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['financeiro']