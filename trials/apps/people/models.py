from django.db import models

from trials.apps.schools.models import School


class Person(models.Model):
    """
    Base class for student, teacher, parent
    """
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Teacher(Person):
    """
    Teacher
    """
    # Fields: school, ...
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    # SHould their be a many to one field for students?


class Student(Person):
    """
    Student
    """
    # Fields: grade, school, teacher, ...
    grade = models.PositiveIntegerField()
    teacher = models.ForeignKey(Teacher)
    school = models.ForeignKey(School)
