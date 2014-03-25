from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.models import User

def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def all(request):
    users = User.objects.filter(is_active=True)
    return render_to_response('all.html', locals(), context_instance=RequestContext(request))