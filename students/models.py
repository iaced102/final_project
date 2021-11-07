from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Student(models.Model):
    student     = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.student)