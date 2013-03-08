from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from resume.forms import ReferenceForm
from resume.models import Reference
from datetime import date

def ReferencePosting(request):
    if request.user.is_authenticated():
        profile = request.user.get_profile()
        if not profile.is_intern:
            return HttpResponseRedirect('/profile')
        form = ReferenceForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                reference_post = add_reference(form, profile)
                return HttpResponseRedirect('/profile')
            else:
                return render_to_response('resume/reference_post.html', {'form': form}, context_instance=RequestContext(request))
        else:
            form = ReferenceForm()
            return render_to_response('resume/reference_post.html', {'form': form}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/register/intern')

def edit(request):
    return HttpResponseRedirect('/')

def add_reference(form, profile):
    reference = Reference()
    reference.profile = profile
    reference.name = form.cleaned_data['name']
    reference.relationship = form.cleaned_data['relationship']
    reference.email = form.cleaned_data['email']
    reference.save()
    return reference
