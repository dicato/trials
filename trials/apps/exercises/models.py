from django.db import models


class Exercise(models.Model):
    """
    An exercise is made up of a set of trails.
    """
    # FIelds: Name, description, date,
    #   teacher, student, set of trials

    name = models.CharField(max_length=256)
    description = models.TextField()
