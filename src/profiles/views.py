from django.shortcuts import render_to_response, RequestContext, Http404
from django.contrib.auth.models import User
from .forms import AddressForm, JobForm, UserPictureForm
from .models import Address, Job, UserPicture
from django.forms.models import modelformset_factory




def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


def all(request):
    users = User.objects.filter(is_active=True)
    return render_to_response('profiles/all.html', locals(), context_instance=RequestContext(request))


def single_user(request, username):
    try:
        user = User.objects.get(username = username)
        if user.is_active:
            single_user = user 
    except Exception:
        raise Http404
    return render_to_response('profiles/single_user.html', locals(), context_instance=RequestContext(request))


def edit_address(request):
    # initialize instances to be modified 
    user = request.user
    addresses = Address.objects.filter(user=user)
    
    # Connect forms to instances
    AddressFormset = modelformset_factory(Address, form=AddressForm, extra=1)
    formset_a = AddressFormset(request.POST or None, queryset=addresses)
    
    ##Actually save the form responses
    if  formset_a.is_valid():
        pass
    
    return render_to_response('profiles/edit_address.html', locals(), context_instance=RequestContext(request))


def edit_job(request):
    # initialize instances to be modified 
    user = request.user
    jobs = Job.objects.filter(user=user)
    
    # Connect forms to instances
    JobFormset = modelformset_factory(Job, form=JobForm, extra=1)
    formset_j = JobFormset(request.POST or None, queryset=jobs)
    
    ##Actually save the form responses
    if  formset_j.is_valid():
        pass

    return render_to_response('profiles/edit_job.html', locals(), context_instance=RequestContext(request))

def edit_profile(request):
    # initialize instances to be modified 
    user = request.user
    addresses = Address.objects.filter(user=user)
    jobs = Job.objects.filter(user=user)
    picture = UserPicture.objects.get(user=user)
    
    # Connect forms to instances
    AddressFormset = modelformset_factory(Address, form=AddressForm, extra=1)
    formset_a = AddressFormset(queryset=addresses)
    
    JobFormset = modelformset_factory(Job, form=JobForm, extra=1)
    formset_j = JobFormset(queryset=jobs)
    
    user_picture_form = UserPictureForm(request.POST or None, request.FILES or None, prefix='picture', instance=picture)
     
    ##Actually save the form responses
    if  user_picture_form.is_valid():
        form = user_picture_form.save(commit=False)
        form.save()
    return render_to_response('profiles/edit_profile.html', locals(), context_instance=RequestContext(request))
