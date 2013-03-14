from django.db import models


class Person(models.Model):
    """
    Base class for student, teacher, parent
    """
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Student(Person):
    """
    Student
    """
    # Fields: grade, school, teacher, ...
    grade = models.PositiveIntegerField()


class Teacher(Person):
    """
    Teacher
    """
    # Fields: school, ...