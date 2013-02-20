from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from account.models import InternProfile, CompanyProfile

#def profile(request):
#   if request.user.is_authenticated():
#       if request.user.is_intern == "Intern":
#           internProfile(request)
#       else:
#           companyProfile(request)
#    else:
#        return HttpResponseRedirect('login/')       

def generateInternProfile(user):
    return render_to_response('account/profile_intern.html', {'intern': user}, context_instance=RequestContext(request))

def generateCompanyProfile(user):
    return render_to_response('account/profile_company.html', {'company': user}, context_instance=RequestContext(request))

#@login_required
def index(request):
    if request.user.is_authenticated():
        user = request.user
        if user.is_intern == "Intern":
            generateInternProfile(user)
        else:
            generateCompanyProfile(user)
#                return render_to_response('templates/profile.html', { 'profile': intern })
        user_profile = request.user.get_profile()
        url = user_profile.url
    else:
        return HttpResponseRedirect('login/')


# We should add some middleware to determine if user is "Company" or "Intern"
