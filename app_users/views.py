from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpRequest , HttpResponseRedirect
from .forms import RegisterForm
from django.urls import reverse

# Create your views here.

def first(request):
    return (render(request,'app_users/first.html'))

def register(request : HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect(reverse("home"))
    else :
        form = RegisterForm()
        
    return (render(request,'app_users/register.html',{'form':form}))
