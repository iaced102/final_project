from django.db import models
from django.contrib.auth import get_user_model
from students.models import Student
from list_class.models import Category_Class
from sessions.models import Session
# Create your models here.

User = get_user_model()

class Time_Session(models.Model):
    monday      = 'Monday'
    tuesday     = 'Tuesday'
    wednesday   = 'Wednesday'
    thursday    = 'Thursday'
    friday      = 'Friday'
    saturday    = 'Saturday'
    sunday      = 'Sunday'
    choice_weekday = [
        (monday,'Monday'),
        (tuesday,'Tuesday'),
        (wednesday,'Wednesday'),
        (thursday,'Thursday'),
        (friday,'Friday'),
        (saturday,'Saturday'),
        (sunday,'Sunday'),
    ]

    weekday_session = models.CharField(max_length=20, choices=choice_weekday)
    time            = models.TimeField(null=True)

    def __str__(self):
        return str(self.time) + ' ' + str(self.weekday_session)




class ClassRoom(models.Model):
    name            = models.CharField(max_length=20)
    teacher         = models.ForeignKey(User, on_delete=models.DO_NOTHING,blank=True, null=True)
    students        = models.ManyToManyField(Student, blank=True)
    is_active       = models.BooleanField(default= False)
    is_complete     = models.BooleanField(default=False)
    type            = models.ForeignKey(Category_Class, on_delete=models.CASCADE)
    expected_active = models.DateField()
    sessions        = models.ManyToManyField(Session,blank=True)
    start_learn     = models.DateField()
    schedule        = models.ManyToManyField(Time_Session)


    def __str__(self):
        return self.name



class Link_Students_to_Students(models.Model):
    student     = models.ForeignKey(User, on_delete=models.CASCADE)
    to_class    = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    def __str__(self):
        return self.student.username



