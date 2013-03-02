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
        profile = user.get_profile()
        if profile.is_intern:
            return render_to_response('account/intern_profile_index.html', {'user': user, 'userProfile': profile}, context_instance=RequestContext(request))
        else:
            return render_to_response('account/company_profile_index.html', {'user': user, 'userProfile': profile}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

def publicCompanyProfile(request, company_id):
    try: # try to get a profile record
        requestedProfile = Profile.objects.get(pk=company_id)
        requestedUser = User.objects.get(id=requestedProfile.user.id)
    except Profile.DoesNotExist:
        raise Http404

    if not requestedProfile.is_intern and requestedUser.is_active:
        if request.user.is_authenticated():
            user = request.user
            profile = user.get_profile()
            return render_to_response('account/company_profile.html', {'user' : user, 'userProfile' : profile, 'profile': requestedProfile}, context_instance=RequestContext(request))
        else:
            return render_to_response('account/company_profile.html', {'user' : None, 'profile': requestedProfile}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

def privateInternProfile(request, intern_id):
    try:
        requestedProfile = Profile.objects.get(user_id=intern_id)
        requestedUser = User.objects.get(id=requestedProfile.user.id)
    except Profile.DoesNotExist:
        raise Http404

    if requestedProfile.is_intern and requestedUser.is_active:
        if request.user.is_authenticated():
            user = request.user
            profile = user.get_profile()
            if profile.is_intern and requestedProfile.id == profile.id: # intern can view his own page
                return render_to_response('account/intern_profile.html', {'user' : user, 'userProfile' : profile, 'profile': requestedProfile}, context_instance=RequestContext(request))
            elif profile.is_intern: # interns can't view profile pages
                return HttpResponseRedirect('/')    
            else: # request to view profile is coming from company
                return render_to_response('account/intern_profile.html', {'user' : user, 'userProfile' : profile, 'profile': requestedProfile}, context_instance=RequestContext(request))
        else: # redirect to login because user is not signed in.
            return HttpResponseRedirect('/login')
    else: # redirect to home because user is not company nor intern
        return HttpResponseRedirect('/')

def settings(request):
    if request.user.is_authenticated():
        user = request.user
        profile = user.get_profile()
        return render_to_response('account/profile_settings.html', {'user': user, 'userProfile' : profile}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

def deactivate(request):
    if request.user.is_authenticated():
        user = request.user
        if user.is_active:
            user.is_active = False
            user.save()
        return HttpResponseRedirect('/logout')
    else:
        return HttpResponseRedirect('/login')

def edit(request):
    if request.user.is_authenticated():
        user = request.user
        profile = user.get_profile()
        return render_to_response('account/profile_edit.html', {'user' : user, 'userProfile' : profile}, context_instance=RequestContext(request))
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
                profile.name = request.POST.get('name')
                profile.school = request.POST.get('school')
                profile.graduation_date = request.POST.get('graduation_date')
                profile.major = request.POST.get('major')
                user.email = request.POST.get('email')
                profile.description = request.POST.get('description')
                user.save()
                profile.save()
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
	    profile = user.get_profile()
        except Profile.DoesNotExist:
            raise Http404
       
        # only companies can post jobs, interns go away...
        if profile.is_intern:
            return redirect('/profile')
        else:
            try:
                postings = profile.jobpost_set.all() 
            except Exception:
                postings = None
            return render_to_response('account/company_profile_jobs.html', {'user': user, 'userProfile': profile, 'postings': postings}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login') # redirect to login page        
