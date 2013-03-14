# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Exercise.datetime'
        db.add_column('exercises_exercise', 'datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Exercise.datetime'
        db.delete_column('exercises_exercise', 'datetime')


    models = {
        'exercises.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Student']"}),
            'trials': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['exercises.Trial']", 'symmetrical': 'False'})
        },
        'exercises.trial': {
            'Meta': {'object_name': 'Trial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prompted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'people.person': {
            'Meta': {'object_name': 'Person'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'people.student': {
            'Meta': {'object_name': 'Student', '_ormbases': ['people.Person']},
            'grade': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['people.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.School']"}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Teacher']"})
        },
        'people.teacher': {
            'Meta': {'object_name': 'Teacher', '_ormbases': ['people.Person']},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['people.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'schools.school': {
            'Meta': {'object_name': 'School'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'homepage': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['exercises']