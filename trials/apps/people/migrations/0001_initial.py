# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('people_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('people', ['Person'])

        # Adding model 'Teacher'
        db.create_table('people_teacher', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['people.Person'], unique=True, primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('people', ['Teacher'])

        # Adding model 'Student'
        db.create_table('people_student', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['people.Person'], unique=True, primary_key=True)),
            ('grade', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Teacher'])),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.School'])),
        ))
        db.send_create_signal('people', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('people_person')

        # Deleting model 'Teacher'
        db.delete_table('people_teacher')

        # Deleting model 'Student'
        db.delete_table('people_student')


    models = {
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

    complete_apps = ['people']