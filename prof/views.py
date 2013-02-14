from prof.models import Prof
from django.http import HttpResponse

def GetInternProfile(request):
	if !request.user.is_authenticated():
		return HttpResponseRedirect('/register/intern')
	if request.method =='GET':
		intern = user.getProfile()
		return render_to_response('templates/profile.html', { 'profile_information': intern }
		
