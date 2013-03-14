from django.db import models


class School(models.Model):
    """
    """
    name = models.CharField(max_length=512)
    address = models.TextField()
    homepage = models.URLField()

    def __unicode__(self):
        return unicode(self.name)
