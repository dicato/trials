# stardard library imports

# django imports
from django.http import Http404, HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

from django.views.generic import (CreateView,
                                  DeleteView,
                                  DetailView,
                                  ListView,
                                  UpdateView)


from trials.apps.people.models import Teacher, Student
from trials.apps.exercises.models import Exercise


class Students(ListView):
    model = Student
    template_name = 'students.html'


class Student(DetailView):
    model = Student
    template_name = 'student.html'
