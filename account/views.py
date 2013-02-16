from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from account.models import InternProfile, CompanyProfile

def sample_intern(request):
    return render_to_response('account/profile_intern.html', {'quiz': 'quiz'}, context_instance=RequestContext(request))

def sample_company(request):
    return render_to_response('account/profile_company.html', {'quiz': 'quiz'}, context_instance=RequestContext(request))

#@login_required
def view_profile(request):
    if request.user.is_authenticated():
#        if request.method == 'GET':
#                intern = user.getProfile()
#                return render_to_response('templates/profile.html', { 'profile': intern })
#    else:
#            return HttpResponseRedirect('/register/intern')
        user_profile = request.user.get_profile()
        url = user_profile.url
    else:
        return HttpResponseRedirect('login/')


# We should add some middleware to determine if user is "Company" or "Intern"
