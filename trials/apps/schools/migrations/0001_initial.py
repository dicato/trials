# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'School'
        db.create_table('schools_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('homepage', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('schools', ['School'])


    def backwards(self, orm):
        # Deleting model 'School'
        db.delete_table('schools_school')


    models = {
        'schools.school': {
            'Meta': {'object_name': 'School'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'homepage': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['schools']