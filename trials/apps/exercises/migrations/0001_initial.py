# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Trial'
        db.create_table('exercises_trial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('success', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('prompted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('exercises', ['Trial'])

        # Adding model 'Exercise'
        db.create_table('exercises_exercise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Student'])),
        ))
        db.send_create_signal('exercises', ['Exercise'])

        # Adding M2M table for field trials on 'Exercise'
        db.create_table('exercises_exercise_trials', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exercise', models.ForeignKey(orm['exercises.exercise'], null=False)),
            ('trial', models.ForeignKey(orm['exercises.trial'], null=False))
        ))
        db.create_unique('exercises_exercise_trials', ['exercise_id', 'trial_id'])


    def backwards(self, orm):
        # Deleting model 'Trial'
        db.delete_table('exercises_trial')

        # Deleting model 'Exercise'
        db.delete_table('exercises_exercise')

        # Removing M2M table for field trials on 'Exercise'
        db.delete_table('exercises_exercise_trials')


    models = {
        'exercises.exercise': {
            'Meta': {'object_name': 'Exercise'},
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