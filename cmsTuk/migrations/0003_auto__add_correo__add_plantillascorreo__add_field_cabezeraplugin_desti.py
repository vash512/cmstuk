# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'correo'
        db.create_table(u'cmsTuk_correo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('correo', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'cmsTuk', ['correo'])

        # Adding model 'plantillasCorreo'
        db.create_table(u'cmsTuk_plantillascorreo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('html', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cmsTuk', ['plantillasCorreo'])

        # Adding field 'cabezeraPlugin.destino'
        db.add_column(u'cmsplugin_cabezeraplugin', 'destino',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsTuk.correo'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'cabezeraPlugin.plantilla'
        db.add_column(u'cmsplugin_cabezeraplugin', 'plantilla',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsTuk.plantillasCorreo'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'cabezeraPlugin.fondo'
        db.alter_column(u'cmsplugin_cabezeraplugin', 'fondo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):
        # Deleting model 'correo'
        db.delete_table(u'cmsTuk_correo')

        # Deleting model 'plantillasCorreo'
        db.delete_table(u'cmsTuk_plantillascorreo')

        # Deleting field 'cabezeraPlugin.destino'
        db.delete_column(u'cmsplugin_cabezeraplugin', 'destino_id')

        # Deleting field 'cabezeraPlugin.plantilla'
        db.delete_column(u'cmsplugin_cabezeraplugin', 'plantilla_id')


        # User chose to not deal with backwards NULL issues for 'cabezeraPlugin.fondo'
        raise RuntimeError("Cannot reverse this migration. 'cabezeraPlugin.fondo' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'cabezeraPlugin.fondo'
        db.alter_column(u'cmsplugin_cabezeraplugin', 'fondo', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

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
        u'cmsTuk.plantillascorreo': {
            'Meta': {'object_name': 'plantillasCorreo'},
            'html': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cmsTuk']