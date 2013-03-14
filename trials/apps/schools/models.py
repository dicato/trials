from django.db import models


class School(models.Model):
    """
    """
    name = models.CharField()
    address = models.CharField()
    homepage = models.URLField()
