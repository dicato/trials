# stardard library imports

# django imports
from django.http import Http404, HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

from trials.apps.people.models import Teacher, Student
from trials.apps.exercises.models import Exercise


def students(request):
    """
    Show all students.
    """
    all = Student.objects.all()
    return render_to_response('students.html', {'students': all})


def student_detail(request, student_id):
    """
    View a student, their details, and their exercises.
    """
    try:
        student = Student.objects.get(id=student_id)
    except:
        raise Http404

    return render_to_response('student.html', {'student': student})
