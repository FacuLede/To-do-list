from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.http import Http404
from tasks.models import Task
# Create your views here.

def home(request) :
    if request.user.is_authenticated :
        data = {
            'completed_tasks':  Task.objects.filter(user = request.user, datecompleted__isnull = False).count(),
            'pending_tasks': Task.objects.filter(user = request.user, datecompleted__isnull = True).count(),
        }
        return render(request, 'home.html', data)
    else :
        return render(request, 'home.html')
    

class Signup(View) :
    
    def get(self, request):
        if request.user.is_authenticated:
            raise Http404("No tienes permiso para acceder a esta página.")
        form = UserCreationForm()
        return render(request, "signup.html",{"form":form})
    
    def post(self, request):
        if request.user.is_authenticated:
            raise Http404("No tienes permiso para acceder a esta página.")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home')
        else :
            for msg in form.error_messages :
                messages.error(request, form.error_messages[msg])
            return render(request, "signup.html",{"form":form})

def log_in(request) :

    if request.user.is_authenticated:
        raise Http404("No tienes permiso para acceder a esta página.")

    if request.method == 'POST' :
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid() :
            username1 = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password")
            user = authenticate(username=username1, password = password1)
            if user is not None :
                login(request, user)
                return redirect('home')
        else:
            messages.error(request,"Alguno de los datos ingresados no es correcto.")
    else :
        form = AuthenticationForm()
    return render(request, "login.html",{"form":form})

@login_required
def log_out(request) :
    logout(request)
    return redirect('home')