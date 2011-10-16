from django.template import RequestContext, Context
from django.http import HttpResponseForbidden, HttpResponse, Http404
from django.shortcuts import render_to_response, redirect

def index(request):
  return render_to_response('index.html', {}, context_instance=RequestContext(request))

