# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Node'
        db.create_table(u'nodes_node', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device_id', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('rssi_data', self.gf('django.db.models.fields.IntegerField')()),
            ('distance', self.gf('django.db.models.fields.IntegerField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('node_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('confidence', self.gf('django.db.models.fields.IntegerField')()),
            ('location_x', self.gf('django.db.models.fields.IntegerField')()),
            ('location_y', self.gf('django.db.models.fields.IntegerField')()),
            ('origin_x', self.gf('django.db.models.fields.IntegerField')()),
            ('origin_y', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'nodes', ['Node'])


    def backwards(self, orm):
        # Deleting model 'Node'
        db.delete_table(u'nodes_node')


    models = {
        u'nodes.node': {
            'Meta': {'object_name': 'Node'},
            'confidence': ('django.db.models.fields.IntegerField', [], {}),
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'distance': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_x': ('django.db.models.fields.IntegerField', [], {}),
            'location_y': ('django.db.models.fields.IntegerField', [], {}),
            'node_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'origin_x': ('django.db.models.fields.IntegerField', [], {}),
            'origin_y': ('django.db.models.fields.IntegerField', [], {}),
            'rssi_data': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['nodes']