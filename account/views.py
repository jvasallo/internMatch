from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from register.models import Profile
from job_post.models import JobPost

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
            return render_to_response('account/edit_xeditable.html', {'intern': user}, context_instance=RequestContext(request))
        else:
            return render_to_response('account/edit_xeditable.html', {'company': user}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def update(request):
    if request.user.is_authenticated(): # if user is logged in https://docs.djangoproject.com/en/dev/topics/forms/?from=olddocs
        user = request.user
        try: # try to get a profile record
            profile = user.get_profile()
        except Profile.DoesNotExist:
            raise Http404
        if request.method == 'POST': # and if request is a POST
            if profile.is_intern:
                print 'hello'
            else:
                profile.name = request.POST.get('name')
                profile.description = request.POST.get('description')
                profile.industry = request.POST.get('industry')
                profile.address = request.POST.get('address')
                profile.city = request.POST.get('city')
                profile.state = request.POST.get('state')
                profile.zip = request.POST.get('zip')
                user.email = request.POST.get('email')
                profile.phone = request.POST.get('contactPhone')
                profile.contactEmail = request.POST.get('contactEmail')
                profile.website = request.POST.get('companyWebsite')
                user.save()
                profile.save()
            return redirect('/profile')
    else: # else user needs to log in
        return HttpResponseRedirect('/login') # redirect to some result page to show the "result"

def jobs(request):
    if request.user.is_authenticated():
        try:
            user = request.user
	    profile = request.user.get_profile()
        except Profile.DoesNotExist:
            raise Http404

        if not profile.is_intern:
            try:
                postings = profile.jobpost_set.all() 
            except Exception:
                postings = None
            return render_to_response('account/company_jobs.html', {'company': user, 'profile': profile, 'postings': postings}, context_instance=RequestContext(request))
        else:
            return redirect('/profile')
    else:
        return HttpResponseRedirect('/login') # redirect to login page        
