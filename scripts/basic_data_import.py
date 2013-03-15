#!/usr/bin/env python

from django.core.management import setup_environ

from trials.apps.schools.models import School
from trials.apps.exercises.models import Exercise
from trials.apps.people.models import Teacher, Student
from trials.settings import dev

setup_environ(dev)


def add_schools():
    s = School()
    s.name = 'Lynnfield High School'
    s.address = '275 Essex St  Lynnfield, MA 01940'
    s.homepage = 'http://www.lynnfield.k12.ma.us/'
    s.save()

    t = School()
    t.name = 'Barrows School'
    t.address = '16 Edgemont Ave, Reading, MA 01867'
    t.homepage = 'http://www.edline.net/pages/Alice_M__Barrows_Elementary_Sc'
    t.save()


def add_people():
    kelly = Teacher()
    kelly.first_name = 'Fake'
    kelly.last_name = 'Teacher'
    kelly.email = 'faketeacher@gmail.com'
    kelly.phone = '7777777777'
    kelly.save()

    student = Student()
    student.first_name = 'Fake'
    student.last_name = 'Student'
    student.grade = 3
    student.teacher = Teacher.objects.get(first_name='Fake')
    student.school = School.objects.get(name=('Barrows School'))
    student.save()


def add_exercises():
    e = Exercise()
    e.name = 'Sample Exercise'
    e.description = 'This is a simple sample exercise.'
    e.student = Student.objects.get(first_name='Fake')
    e.save()


def main():
    add_schools()
    add_people()
    add_exercises()


if __name__ == '__main__':
    main()
