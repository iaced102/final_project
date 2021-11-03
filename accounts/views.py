from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
# Create your views here.


def RegistrationView(request):
    form = RegistrationForm()
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            account = authenticate(username=username, password=password)
            login(request, account)
            return redirect('home')

    context = {'form':form}
    return render(request,'registrations/signup.html', context)


class Profile(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
