from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Category_Class
from classroom.models import ClassRoom
from django.db.models import Q
# Create your views here.

class List_Category_Class(TemplateView):
    template_name ='apps/list_category_class.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_class'] = Category_Class.objects.all()
        context['register_class'] = ClassRoom.objects.filter(is_active=False)
        context['list_category_class']= Category_Class.objects.all()
        context['list_classroom'] = ClassRoom.objects.filter(is_active=False)
        return context

        
def List_Class_of_Category(request,type):
    context = {}
    context['detail_category'] = Category_Class.objects.filter(type= type)[0]
    
    query = Q(type__type=type)
    query.add(Q(is_active=False), Q.AND)
    context['list_class_of_category'] = ClassRoom.objects.filter(query)
    context['list_category_class']= Category_Class.objects.all()
    context['list_classroom'] = ClassRoom.objects.filter(is_active=False)
    return render(request, 'apps/list-class-of-category.html', context)