from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from register.forms import InternRegistrationForm, CompanyRegistrationForm
from django.contrib.contenttypes.models import ContentType
from register.models import Profile

def InternRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    if request.method == 'POST':
        form = InternRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'],)
            user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            profile = user.get_profile()
            profile.name = form.cleaned_data['name']
            profile.school = form.cleaned_data['school']
            profile.graduation_date = form.cleaned_data['graduation_date']
            profile.major = form.cleaned_data['major']
            profile.is_intern = True           
            profile.save()
            return HttpResponseRedirect('/quiz/begin')
        else:
            return render_to_response('register/registration.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = InternRegistrationForm()
        context = {'form': form}
        return render_to_response('register/registration.html', context, context_instance=RequestContext(request))
    
def CompanyRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'],)
            user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            company = user.get_profile()
            company.name = form.cleaned_data['name']
            company.is_intern = False
            company.save()
            return HttpResponseRedirect('/quiz/begin')
        else:
            return render_to_response('register/registration.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = CompanyRegistrationForm()
        context = {'form': form}
        return render_to_response('register/registration.html', context, context_instance=RequestContext(request))
