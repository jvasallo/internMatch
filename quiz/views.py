from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from quiz.models import Quiz

def index(request):
    quiz = Quiz.objects.get(id=1)
    return render_to_response('quiz/quiz.html', {'quiz': quiz}, context_instance=RequestContext(request))

@csrf_exempt
def submit(request):
   # django.middleware.csrf.get_token(request)
#    import pdb; pdb.set_trace()
    if request.user.is_authenticated(): # if user is logged in https://docs.djangoproject.com/en/dev/topics/forms/?from=olddocs
        if request.method == 'POST': # and if request is a POST
            q = Quiz.create(request.user.user_id)  # init a null quiz result
            q.collectQuizData(request.POST) # use the request to sent the data to the def collectQuizData
        return HttpResponseRedirect('complete/') # redirect to a thank you page or something
    else: # else user needs to log in
	print request.POST["[%USER_ID_HERE%] 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19"]
        return HttpResponseRedirect('/login')
        #return render_to_response('intern_registration.html', {'form' : 'context'}) # redirect them back to the registration page or error page.
#    return HttpResponse("You're submission is recorded as %s" % quiz_id)
