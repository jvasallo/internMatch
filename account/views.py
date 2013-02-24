from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from register.models import Profile

def index(request):
    if request.user.is_authenticated():
        user = request.user
        userProfile = request.user.get_profile()
        if userProfile.is_intern:
            return render_to_response('account/profile_intern.html', {'intern': user}, context_instance=RequestContext(request))
        else:
            return render_to_response('account/profile_company.html', {'company': user}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

def publicCompanyProfile(request, company_id):
    try:
        companyProfile = Profile.objects.get(pk=company_id)
    except JobPost.DoesNotExist:
        raise Http404
    return render_to_response('account/profile_company.html', {'company': companyProfile}, context_instance=RequestContext(request))

def add(request):
    if request.user.is_authenticated():
        user = request.user
        userProfile = request.user.get_profile()
        if userProfile.is_intern:
            return render_to_response('account/add.html', {'intern': user}, context_instance=RequestContext(request))
        else:
            return render_to_response('account/add.html', {'company': user}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

def edit(request):
    if request.user.is_authenticated():
        user = request.user
        userProfile = request.user.get_profile()
        if userProfile.is_intern:
            return render_to_response('account/edit.html', {'intern': user}, context_instance=RequestContext(request))
        else:
            return render_to_response('account/edit.html', {'company': user}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')
