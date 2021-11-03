from django.urls import path
from .views import Infor_Class, Join_To_Class, classroom, in_session

urlpatterns = [
    path('<int:pk>', Infor_Class.as_view(), name='infor_class'),
    path('join_to_class/', Join_To_Class, name='join_to_class'),
    path('classroom/<int:pk>', classroom, name='to_classroom'),
    path('session/<int:id>',in_session, name='in_session')
]