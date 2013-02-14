from django.http import HttpResponseRedirect
from prof.models import Prof

def GetInternProfile(request):
	if request.user.is_authenticated():
	    if request.method == 'GET':
		    intern = user.getProfile()
		    return render_to_response('templates/profile.html', { 'profile': intern })
	else:
		return HttpResponseRedirect('/register/intern')