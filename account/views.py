from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from account.models import InternProfile, CompanyProfile

def index(request):
    if request.user.is_authenticated():
        user = request.user
        userProfile = request.user.get_profile()
        if userProfile.is_intern:
            return render_to_response('account/profile_intern.html', {'intern': user}, context_instance=RequestContext(request))
        else:
            return render_to_response('account/profile_company.html', {'company': user}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('login/')

def add(request):
    if request.user.is_authenticated():
        user = request.user
        userProfile = request.user.get_profile()
        if userProfile.is_intern:
            return render_to_response('account/add.html', {'intern': user}, context_instance=RequestContext(request))
        else:
            return render_to_response('account/add.html', {'company': user}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('login/')
