from datetime import datetime

from django.db import models

from trials.apps.people.models import Student


class Trial(models.Model):
    """
    An individual trial
    """
    success = models.BooleanField()
    prompted = models.BooleanField()

    def __unicode__(self):
        if self.success and self.prompted:
            return u'++'
        elif self.success and not self.prompted:
            return u'+-'
        elif not self.success and self.prompted:
            return u'-+'
        else:
            return u'--'


class Exercise(models.Model):
    """
    An exercise is made up of a set of trails.
    """
    # FIelds: Name, description, date,
    #   teacher, student, set of trials

    name = models.CharField(max_length=256)
    description = models.TextField()
    trials = models.ManyToManyField(Trial)
    student = models.ForeignKey(Student)
    datetime = models.DateTimeField(auto_now_add=True, default=datetime.now)

    def __unicode__(self):
        return unicode(self.name)
