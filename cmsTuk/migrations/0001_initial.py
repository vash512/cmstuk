# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'botonClass'
        db.create_table(u'cmsTuk_botonclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clase', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'cmsTuk', ['botonClass'])

        # Adding model 'botonIcono'
        db.create_table(u'cmsTuk_botonicono', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('icono', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'cmsTuk', ['botonIcono'])

        # Adding model 'plantillasCorreo'
        db.create_table(u'cmsTuk_plantillascorreo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('html', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'cmsTuk', ['plantillasCorreo'])

        # Adding model 'correo'
        db.create_table(u'cmsTuk_correo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('correo', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'cmsTuk', ['correo'])

        # Adding model 'headerPlugin'
        db.create_table(u'cmsplugin_headerplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('boton1', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('clase1', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='boton1_clase', null=True, to=orm['cmsTuk.botonClass'])),
            ('icono1', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='boton1_icono', null=True, to=orm['cmsTuk.botonIcono'])),
            ('texto1', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('href1', self.gf('django.db.models.fields.CharField')(default='#', max_length=255, null=True, blank=True)),
            ('boton2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('clase2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='boton2_clase', null=True, to=orm['cmsTuk.botonClass'])),
            ('icono2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='boton2_icono', null=True, to=orm['cmsTuk.botonIcono'])),
            ('texto2', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('href2', self.gf('django.db.models.fields.CharField')(default='#', max_length=255, null=True, blank=True)),
            ('boton3', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('clase3', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='boton3_clase', null=True, to=orm['cmsTuk.botonClass'])),
            ('icono3', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='boton3_icono', null=True, to=orm['cmsTuk.botonIcono'])),
            ('texto3', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('href3', self.gf('django.db.models.fields.CharField')(default='#', max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'cmsTuk', ['headerPlugin'])

        # Adding model 'cabezeraPlugin'
        db.create_table(u'cmsplugin_cabezeraplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('encabezado', self.gf('django.db.models.fields.TextField')()),
            ('fondo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('correo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('destino', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsTuk.correo'], null=True, blank=True)),
            ('plantilla', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsTuk.plantillasCorreo'], null=True, blank=True)),
            ('placeholderEmail', self.gf('django.db.models.fields.CharField')(default='Tu direcci\xc3\xb3n de e@mail.com para informarte', max_length=255, null=True, blank=True)),
            ('subtexto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'cmsTuk', ['cabezeraPlugin'])

        # Adding model 'idioma'
        db.create_table(u'cmsTuk_idioma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idioma', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'cmsTuk', ['idioma'])

        # Adding model 'socialmediaPlugin'
        db.create_table(u'cmsplugin_socialmediaplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('videoYT', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('canal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('twitterText', self.gf('django.db.models.fields.CharField')(max_length=110, null=True, blank=True)),
            ('via', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('idioma', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsTuk.idioma'], null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('foursquare', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('googleplus', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'cmsTuk', ['socialmediaPlugin'])

        # Adding model 'carroManual'
        db.create_table(u'cmsplugin_carromanual', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('mostrar', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('comentario', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tituloF', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('textoF', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tituloBoton', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'cmsTuk', ['carroManual'])

        # Adding model 'bloqueCarroM'
        db.create_table(u'cmsTuk_bloquecarrom', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inline_ordering_position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('carroM', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsTuk.carroManual'], null=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cmsTuk', ['bloqueCarroM'])


    def backwards(self, orm):
        # Deleting model 'botonClass'
        db.delete_table(u'cmsTuk_botonclass')

        # Deleting model 'botonIcono'
        db.delete_table(u'cmsTuk_botonicono')

        # Deleting model 'plantillasCorreo'
        db.delete_table(u'cmsTuk_plantillascorreo')

        # Deleting model 'correo'
        db.delete_table(u'cmsTuk_correo')

        # Deleting model 'headerPlugin'
        db.delete_table(u'cmsplugin_headerplugin')

        # Deleting model 'cabezeraPlugin'
        db.delete_table(u'cmsplugin_cabezeraplugin')

        # Deleting model 'idioma'
        db.delete_table(u'cmsTuk_idioma')

        # Deleting model 'socialmediaPlugin'
        db.delete_table(u'cmsplugin_socialmediaplugin')

        # Deleting model 'carroManual'
        db.delete_table(u'cmsplugin_carromanual')

        # Deleting model 'bloqueCarroM'
        db.delete_table(u'cmsTuk_bloquecarrom')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsTuk.bloquecarrom': {
            'Meta': {'ordering': "('inline_ordering_position',)", 'object_name': 'bloqueCarroM'},
            'carroM': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmsTuk.carroManual']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inline_ordering_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'cmsTuk.botonclass': {
            'Meta': {'object_name': 'botonClass'},
            'clase': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cmsTuk.botonicono': {
            'Meta': {'object_name': 'botonIcono'},
            'icono': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cmsTuk.cabezeraplugin': {
            'Meta': {'object_name': 'cabezeraPlugin', 'db_table': "u'cmsplugin_cabezeraplugin'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'correo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destino': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmsTuk.correo']", 'null': 'True', 'blank': 'True'}),
            'encabezado': ('django.db.models.fields.TextField', [], {}),
            'fondo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'placeholderEmail': ('django.db.models.fields.CharField', [], {'default': "'Tu direcci\\xc3\\xb3n de e@mail.com para informarte'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'plantilla': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmsTuk.plantillasCorreo']", 'null': 'True', 'blank': 'True'}),
            'subtexto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cmsTuk.carromanual': {
            'Meta': {'object_name': 'carroManual', 'db_table': "u'cmsplugin_carromanual'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'comentario': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mostrar': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'textoF': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tituloBoton': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tituloF': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'cmsTuk.correo': {
            'Meta': {'object_name': 'correo'},
            'correo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cmsTuk.headerplugin': {
            'Meta': {'object_name': 'headerPlugin', 'db_table': "u'cmsplugin_headerplugin'", '_ormbases': ['cms.CMSPlugin']},
            'boton1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'boton2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'boton3': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'clase1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'boton1_clase'", 'null': 'True', 'to': u"orm['cmsTuk.botonClass']"}),
            'clase2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'boton2_clase'", 'null': 'True', 'to': u"orm['cmsTuk.botonClass']"}),
            'clase3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'boton3_clase'", 'null': 'True', 'to': u"orm['cmsTuk.botonClass']"}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href1': ('django.db.models.fields.CharField', [], {'default': "'#'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'href2': ('django.db.models.fields.CharField', [], {'default': "'#'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'href3': ('django.db.models.fields.CharField', [], {'default': "'#'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'icono1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'boton1_icono'", 'null': 'True', 'to': u"orm['cmsTuk.botonIcono']"}),
            'icono2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'boton2_icono'", 'null': 'True', 'to': u"orm['cmsTuk.botonIcono']"}),
            'icono3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'boton3_icono'", 'null': 'True', 'to': u"orm['cmsTuk.botonIcono']"}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'texto1': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'texto2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'texto3': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cmsTuk.idioma': {
            'Meta': {'object_name': 'idioma'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cmsTuk.plantillascorreo': {
            'Meta': {'object_name': 'plantillasCorreo'},
            'html': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cmsTuk.socialmediaplugin': {
            'Meta': {'object_name': 'socialmediaPlugin', 'db_table': "u'cmsplugin_socialmediaplugin'", '_ormbases': ['cms.CMSPlugin']},
            'canal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'foursquare': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'googleplus': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'idioma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmsTuk.idioma']", 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'twitterText': ('django.db.models.fields.CharField', [], {'max_length': '110', 'null': 'True', 'blank': 'True'}),
            'via': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'videoYT': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsTuk']