from django.db.models.fields import DateField
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.urls import reverse
from django.db.models import Q, query
from .models import ClassRoom, Link_Students_to_Students
from students.models import Student
from list_class.models import Category_Class
from sessions.models import Session
from base import auto_create_sessions
import datetime
# Create your views here.

class Infor_Class(DetailView):
    model = ClassRoom
    template_name = 'apps/infor_class.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['list_category_class']= Category_Class.objects.all()
        context['list_classroom'] = ClassRoom.objects.filter(is_active=False)
        return context
    

    

def Join_To_Class(request):
    class_id = request.POST.get('class')
    user = request.user
    for a in ClassRoom.objects.get(id=class_id).students.all():
        if user.username == a.student.username:

            for a in ClassRoom.objects.get(id=class_id).sessions.all():
                return HttpResponse('tml nay o trong lop roi')
            auto_create_sessions(ClassRoom.objects.get(id=class_id))
            return HttpResponse('tml nay o trong lop roi')

    ClassRoom.objects.get(id=class_id).students.add(Student.objects.get(student=user))

    for a in ClassRoom.objects.get(id=class_id).sessions.all():
        return HttpResponse('success')

    auto_create_sessions(ClassRoom.objects.get(id=class_id))
    return HttpResponse('success')


def classroom(request, pk):
    context = {}
    context['class'] = ClassRoom.objects.get(id=pk)
    context['today'] = datetime.datetime.today().date
    return render(request, 'apps/in_class.html', context)


def in_session(request, id):
    context = {}
    context['session'] = Session.objects.get(id=id)
    context['today'] = datetime.datetime.today().date
    return render(request, 'apps/in_session.html', context)

def attendace(request):
    if request.method == 'POST':
        Class = ClassRoom.objects.get(sessions__id = request.POST['session'])
        print(Class)
        qurey = Q(student__id=request.POST["user"])
        qurey.add(Q(to_class=Class), Q.AND)
        session = Session.objects.get(id=request.POST['session'])
        attendace = Link_Students_to_Students.objects.get(qurey)
        attendace.attendance.add(session)
        return HttpResponse('a')