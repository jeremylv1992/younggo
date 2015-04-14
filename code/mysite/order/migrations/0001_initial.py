# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Address'
        db.create_table('order_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('second_tel', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('addr', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('order', ['Address'])


    def backwards(self, orm):
        
        # Deleting model 'Address'
        db.delete_table('order_address')


    models = {
        'order.address': {
            'Meta': {'object_name': 'Address'},
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'second_tel': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['order']
