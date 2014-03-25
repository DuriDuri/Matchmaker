from django.shortcuts import render_to_response, RequestContext, Http404
from django.contrib.auth.models import User



def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def all(request):
    users = User.objects.filter(is_active=True)
    return render_to_response('all.html', locals(), context_instance=RequestContext(request))

def single_user(request, username):
    try:
        user = User.objects.get(username = username)
        if user.is_active:
            single_user = user 
    except Exception:
        raise Http404
    return render_to_response('single_user.html', locals(), context_instance=RequestContext(request))