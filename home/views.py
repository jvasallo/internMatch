from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from register.models import Profile
from home.forms import SigninForm

def index(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', {'user': request.user}, context_instance=RequestContext(request))
    else:
        return render_to_response('index.html', {'user':None}, context_instance=RequestContext(request))

def contact(request):
    if request.user.is_authenticated():
        return render_to_response('contact.html', {'user': request.user}, context_instance=RequestContext(request))
    else:
        return render_to_response('contact.html', {'user':None}, context_instance=RequestContext(request))

def about(request):
    if request.user.is_authenticated():
        return render_to_response('about.html', {'user': request.user}, context_instance=RequestContext(request))
    else:
        return render_to_response('about.html', {'user':None}, context_instance=RequestContext(request))

def Login(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            profile = Profile.objects.get(user_id=user.id)
            if request.user.is_authenticated():
                return HttpResponseRedirect('/profile')
        else:
            return render_to_response('signin.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = SigninForm()
        context = {'form': form}
        return render_to_response('signin.html', context, context_instance=RequestContext(request))

def Logout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
