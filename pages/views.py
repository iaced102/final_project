from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Q
from list_class.models import Category_Class
from classroom.models import ClassRoom, Link_Students_to_Students
from datetime import date, timedelta

User = get_user_model()

# Create your views here.

def HomePage(request):
    context={}
    print('get home')
    context['counter_students']= len(User.objects.filter(is_teacher=False))
    context['counter_teachers']= len(User.objects.filter(is_teacher=True))
    context['list_category_class']= Category_Class.objects.all()
    context['list_classroom'] = ClassRoom.objects.filter(is_active=False)
    return render(request, 'apps/pages/home.html', context=context)

def Profile_User(request, username):
    context = {}
    list_class_of_user_is_not_complete = Q(student__username = username)
    list_class_of_user_is_not_complete.add(Q(to_class__is_complete = False), Q.AND)
    context['list_class_of_user_is_not_complete'] = Link_Students_to_Students.objects.filter(list_class_of_user_is_not_complete)
    list_class_of_user_is_complete = Q(student__username = username)
    list_class_of_user_is_complete.add(Q(to_class__is_complete = True), Q.AND)
    context['list_class_of_user_is_complete'] =Link_Students_to_Students.objects.filter(list_class_of_user_is_complete)
    if len(context['list_class_of_user_is_not_complete']) != 0:
        today = date.today()
        list_day_session = []
        for Class in context['list_class_of_user_is_not_complete']:
            for session in Class.to_class.sessions.all():
                list_day_session.append([Class, session.date, session.time]) 
        weekday=[]
        for i in list_day_session:
            if i[1] >= today - timedelta(days=today.weekday()) and i[1] <= today - timedelta(days=today.weekday()) + timedelta(days=6):
                weekday.append([i[0],str(i[1]),str(i[2]),i[1].weekday()])
        context['schedule'] = weekday
        print(weekday)
    return render(request, 'apps/pages/profile.html', context=context)