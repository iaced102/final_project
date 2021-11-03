from django.urls import path
from .views import HomePage, Profile_User

urlpatterns = [
    path('profile/<str:username>/',Profile_User, name='profile'),
    path('', HomePage, name='home'),
    
]