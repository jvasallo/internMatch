from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from register.models import Profile

def index(request):
    if request.user.is_authenticated():
        user = request.user
        userProfile = request.user.get_profile()
        if userProfile.is_intern:
            return render_to_response('account/profile_intern.html', {'intern': user, 'profile': userProfile}, context_instance=RequestContext(request))
        else:
            return render_to_response('account/profile_company.html', {'company': user, 'profile': userProfile}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

def publicCompanyProfile(request, company_id):
    try: # try to get a profile record
        companyProfile = Profile.objects.get(pk=company_id)
    except Profile.DoesNotExist:
        raise Http404
    if companyProfile.is_intern: # if the companyProfile retrieved is flagged as an intern....
        return HttpResponseRedirect('/')
    else: # else we have an actual company profile so display it.
        return render_to_response('account/profile_company.html', {'company': companyProfile}, context_instance=RequestContext(request))

def privateInternProfile(request, intern_id):
    if request.user.is_authenticated():
        userProfile = request.user.get_profile()
        if userProfile.is_intern: # interns can't view profile pages
            return HttpResponseRedirect('/')    
        else: # request to view profile is coming from company
            try:
                internProfile = Profile.objects.get(pk=intern_id)
            except Profile.DoesNotExist:
                raise Http404
            return render_to_response('account/profile_intern.html', {'intern': internProfile}, context_instance=RequestContext(request))
    else: # redirect to home because user is not company nor intern
        return HttpResponseRedirect('/')

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
