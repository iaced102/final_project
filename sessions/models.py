from django.db import models

# Create your models here.


class Session(models.Model):
    name                = models.CharField(max_length=20)
    date                = models.DateField()
    time                = models.TimeField()
    link_zoom           = models.CharField(max_length=120, null=True)
    id_meeting          = models.CharField(max_length=30, null=True)
    password_meeting    = models.CharField(max_length=10, null=True)
    record_zoom         = models.CharField(max_length=120, blank=True, null=True)
    password_record     = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name