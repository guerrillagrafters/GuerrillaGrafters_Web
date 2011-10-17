# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from main.forms import *
from django.contrib.auth import authenticate, login

def index(request):
    return render_to_response("index.html", {}, RequestContext(request))

def register(request):
    print request.POST
    csrfContext = RequestContext(request)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=new_user.username,
                                    password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect("/")
    else:
        form = CustomUserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    }, csrfContext)
