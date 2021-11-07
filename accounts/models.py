from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone_number    = models.CharField(max_length=20, blank= True)
    first_name      = models.CharField(max_length=20, null=True)
    last_name       = models.CharField(max_length=20, null=True)
    is_teacher      = models.BooleanField(default=False)
    def __str__(self) -> str:
        return str(self.first_name) + ' ' + str(self.last_name)