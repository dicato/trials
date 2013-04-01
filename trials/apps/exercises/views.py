# stardard library imports

# django imports
from django.views.generic import (CreateView,
                                  DeleteView,
                                  DetailView,
                                  ListView,
                                  UpdateView)

from trials.apps.exercises.models import Exercise


class ExerciseList(ListView):
    model = Exercise
    template_name = 'exercise_list.html'


class ExerciseDetail(DetailView):
    model = Exercise
    template_name = 'exercise_detail.html'
