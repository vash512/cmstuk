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


    def backwards(self, orm):
        # Deleting model 'botonClass'
        db.delete_table(u'cmsTuk_botonclass')

        # Deleting model 'botonIcono'
        db.delete_table(u'cmsTuk_botonicono')

        # Deleting model 'headerPlugin'
        db.delete_table(u'cmsplugin_headerplugin')


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
        }
    }

    complete_apps = ['cmsTuk']