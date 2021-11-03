from django.urls import path
from .views import List_Category_Class, List_Class_of_Category

urlpatterns = [
    path('', List_Category_Class.as_view(), name='list_courses'),
    path('<str:type>/',List_Class_of_Category, name='list_class_catgory')
]