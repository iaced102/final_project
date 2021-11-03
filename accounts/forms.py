from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model



class ManageUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','password1','password2', 'phone_number','first_name','last_name','email']