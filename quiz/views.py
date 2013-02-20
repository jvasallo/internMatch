from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from quiz.models import Quiz

def index(request):
    if request.user.is_authenticated():
        quiz = Quiz.objects.get(id=1)
        return render_to_response('quiz/quiz.html', {'quiz': quiz}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login') # redirect to some result page to show the "result"


@csrf_exempt
def submit(request):
    if request.user.is_authenticated(): # if user is logged in https://docs.djangoproject.com/en/dev/topics/forms/?from=olddocs
        if request.method == 'POST': # and if request is a POST
         #   q = Quiz.create(request.user.user_id)  # init a null quiz result
         #   q.collectQuizData(request.POST) # use the request to sent the data to the def collectQuizData
            return HttpResponseRedirect('quiz/complete/') # redirect to a thank you page or something
    else: # else user needs to log in
        return HttpResponseRedirect('/login') # redirect to some result page to show the "result"
