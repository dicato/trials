from trials.apps.exercises.models import Trial, Exercise
from django.contrib import admin


class TrialInline(admin.TabularInline):
    model = Trial


class ExerciseAdmin(admin.ModelAdmin):
    inlines = [TrialInline]


admin.site.register(Trial)
admin.site.register(Exercise, ExerciseAdmin)
