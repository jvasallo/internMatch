from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from quiz.models import QuizResult

def index(request):
    if request.user.is_authenticated():
        user = request.user
        userProfile = request.user.get_profile()
        if userProfile.is_intern:
            return render_to_response('search/company_search.html', {'intern': user}, context_instance=RequestContext(request))
        else:
            return render_to_response('search/intern_search.html', {'company': user}, context_instance=RequestContext(request))
    else:
        return render_to_response('search/company_search.html', {'intern': None}, context_instance=RequestContext(request))
