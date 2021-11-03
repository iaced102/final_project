from django.contrib import admin
from .models import ClassRoom, Link_Students_to_Students,Time_Session
# Register your models here.

admin.site.register(ClassRoom)
admin.site.register(Link_Students_to_Students)
admin.site.register(Time_Session)