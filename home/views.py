from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from register.models import Profile
from home.forms import SigninForm


def Login(request):
#    if request.user.is_authenticated():
#        return HttpResponseRedirect('/profile/intern')
    #user = authenticate(username=request.POST['username'], password=request.POST['password'])
#    import pdb; pdb.set_trace()
    if request.method == 'POST':
#        import pdb; pdb.set_trace()
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            profile = Profile.objects.get(user_id=user.id)
            if request.user.is_authenticated() and profile.is_intern:
                return HttpResponseRedirect('/profile/intern')
            if request.user.is_authenticated() and not profile.is_intern:
                return HttpResponseRedirect('/profile/company')
        else:
            return render_to_response('signin.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = SigninForm()
        context = {'form': form}
        return render_to_response('signin.html', context, context_instance=RequestContext(request))

def Logout(request):
    #import pdb; pdb.set_trace()
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/')
