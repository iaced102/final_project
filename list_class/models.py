from django.db import models

# Create your models here.

class Category_Class(models.Model):
    type                = models.CharField(max_length=20)
    price               = models.CharField(max_length=15,default='')
    description         = models.TextField(default= '')
    number_sessions     = models.PositiveIntegerField(default=20)
    description_image   = models.ImageField(upload_to='static/image/description_course')
    def __str__(self):
        return self.type