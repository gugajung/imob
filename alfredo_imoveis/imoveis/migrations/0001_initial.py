# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Imovel'
        db.create_table(u'imoveis_imovel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('endereco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['enderecos.Endereco'])),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('cod_ref_site', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('valor_iptu', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('valor_aluguel', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('valor_condominio', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=2)),
            ('ultima_vistoria', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('vencimento_iptu', self.gf('django.db.models.fields.DateField')()),
            ('data_cadastro', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('data_last_pag_iptu', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('proprietario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tipo_imovel', self.gf('django.db.models.fields.CharField')(default='R', max_length=1)),
            ('area_construida', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('area_lote', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('local_chaves', self.gf('django.db.models.fields.CharField')(default='I', max_length=1, null=True, blank=True)),
            ('horario_visitas', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('pavimentos', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'imoveis', ['Imovel'])

        # Adding model 'ContratoLocacao'
        db.create_table(u'imoveis_contratolocacao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imovel', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['imoveis.Imovel'], unique=True)),
            ('inicio_contrato', self.gf('django.db.models.fields.DateField')()),
            ('termino_contrato', self.gf('django.db.models.fields.DateField')()),
            ('data_emissao_contrato', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('locatario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='locatario_contrato', to=orm['clientes.Cliente'])),
            ('fiador1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fiador1_contrato', to=orm['clientes.Cliente'])),
            ('fiador2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fiador2_contrato', null=True, to=orm['clientes.Cliente'])),
            ('fiador3', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fiador3_contrato', null=True, to=orm['clientes.Cliente'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
            ('tipo_contrato', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('observacao', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('gerou_receber', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'imoveis', ['ContratoLocacao'])

        # Adding model 'ContratoAdministrativo'
        db.create_table(u'imoveis_contratoadministrativo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imovel', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['imoveis.Imovel'], unique=True)),
            ('inicio_contrato', self.gf('django.db.models.fields.DateField')()),
            ('termino_contrato', self.gf('django.db.models.fields.DateField')()),
            ('data_emissao_contrato', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
        ))
        db.send_create_signal(u'imoveis', ['ContratoAdministrativo'])

        # Adding model 'LaudoVistoria'
        db.create_table(u'imoveis_laudovistoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imovel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imoveis.Imovel'])),
            ('data_vistoria', self.gf('django.db.models.fields.DateField')()),
            ('pintura_interna', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('pintura_externa', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ferragens', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('cores', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('tipo_tinta', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('lampadas_comuns', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('lustres', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('globos', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('lampadas_fluorecentes', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('interruptores', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('luminarias', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('espelho_banheiro', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('campainha', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ar_condicionado', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('instalacao', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('portao_eletronico', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('torneiras', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('chuveiro', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('vaso', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('lavatorio', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('tanque', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('bide', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('descarga', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('box', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('rede_esgoto', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('tacos', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('pisos', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ceramico', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('paredes', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('azulejos', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('vidros', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('portas', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fechaduras', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('trincos', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('janelas', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('muros', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('grades', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('telhado', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('forro', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('laje', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('portao', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('armarios', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('guarda_roupas', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('chaves', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('cerca_eletrica', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('observacao', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'imoveis', ['LaudoVistoria'])

        # Adding model 'RescisaoContrato'
        db.create_table(u'imoveis_rescisaocontrato', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contrato', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['imoveis.ContratoLocacao'], unique=True)),
            ('motivo', self.gf('django.db.models.fields.TextField')()),
            ('data', self.gf('django.db.models.fields.DateField')()),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'imoveis', ['RescisaoContrato'])


    def backwards(self, orm):
        # Deleting model 'Imovel'
        db.delete_table(u'imoveis_imovel')

        # Deleting model 'ContratoLocacao'
        db.delete_table(u'imoveis_contratolocacao')

        # Deleting model 'ContratoAdministrativo'
        db.delete_table(u'imoveis_contratoadministrativo')

        # Deleting model 'LaudoVistoria'
        db.delete_table(u'imoveis_laudovistoria')

        # Deleting model 'RescisaoContrato'
        db.delete_table(u'imoveis_rescisaocontrato')


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
        u'imoveis.contratoadministrativo': {
            'Meta': {'object_name': 'ContratoAdministrativo'},
            'data_emissao_contrato': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imovel': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['imoveis.Imovel']", 'unique': 'True'}),
            'inicio_contrato': ('django.db.models.fields.DateField', [], {}),
            'termino_contrato': ('django.db.models.fields.DateField', [], {})
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
        },
        u'imoveis.laudovistoria': {
            'Meta': {'object_name': 'LaudoVistoria'},
            'ar_condicionado': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'armarios': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'azulejos': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bide': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'box': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'campainha': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ceramico': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cerca_eletrica': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'chaves': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'chuveiro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cores': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'data_vistoria': ('django.db.models.fields.DateField', [], {}),
            'descarga': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'espelho_banheiro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fechaduras': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ferragens': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'forro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'globos': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'grades': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'guarda_roupas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imovel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['imoveis.Imovel']"}),
            'instalacao': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'interruptores': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'janelas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'laje': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lampadas_comuns': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lampadas_fluorecentes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lavatorio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'luminarias': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lustres': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'muros': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'observacao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'paredes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pintura_externa': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pintura_interna': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pisos': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'portao': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'portao_eletronico': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'portas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rede_esgoto': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tacos': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tanque': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'telhado': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tipo_tinta': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'torneiras': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'trincos': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'vaso': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'vidros': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'imoveis.rescisaocontrato': {
            'Meta': {'object_name': 'RescisaoContrato'},
            'contrato': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['imoveis.ContratoLocacao']", 'unique': 'True'}),
            'data': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.TextField', [], {}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['imoveis']