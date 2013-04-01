# stardard library imports

# django imports
from django.views.generic import (CreateView,
                                  DeleteView,
                                  DetailView,
                                  ListView,
                                  UpdateView)


from trials.apps.people.models import Teacher, Student


class StudentList(ListView):
    model = Student
    template_name = 'student_list.html'


class StudentDetail(DetailView):
    model = Student
    template_name = 'student_detail.html'
