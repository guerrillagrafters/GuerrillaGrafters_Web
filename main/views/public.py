# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from main.forms import *
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate, login

def index(request):
    authenticationForm = CustomAuthenticationForm(label_suffix='')
    registrationForm = CustomUserCreationForm(label_suffix='')
    
    return render_to_response("index.html", {'authenticationForm': authenticationForm, 'registrationForm': registrationForm}, RequestContext(request))

def register(request):
    csrfContext = RequestContext(request)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, label_suffix='')
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=new_user.username,
                                    password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect("/")
    else:
        form = CustomUserCreationForm(label_suffix='')
    return render_to_response("registration/register.html", {
        'registrationForm': form,
    }, csrfContext)
