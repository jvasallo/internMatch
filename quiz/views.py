from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from quiz.models import Quiz, QuizResult

def index(request):
    if request.user.is_authenticated():
        return render_to_response('quiz/index.html', {'user': request.user}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

def quiz(request):
    if request.user.is_authenticated():
        quiz = Quiz.objects.get(id=1)
        user = request.user
        return render_to_response('quiz/quiz.html', {'quiz': quiz, 'user': user}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

def complete(request):
    if request.user.is_authenticated():
        return render_to_response('quiz/complete.html', {'user': request.user}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def submit(request):
    if request.user.is_authenticated(): # if user is logged in https://docs.djangoproject.com/en/dev/topics/forms/?from=olddocs
        user = request.user
        if request.method == 'POST': # and if request is a POST
            quiz = Quiz.objects.get(id=int(request.POST.get('quizID').encode('ascii','ignore')))
            try:
                user_quizresult = QuizResult.objects.get(user=user)
            except Exception:
                user_quizresult = None

            if user_quizresult:
                quizData = str(request.POST.get('quizString').encode('ascii','ignore'))
                user_quizresult.collectQuizData(quizData)
            else:
                user_quizresult = QuizResult.create(quiz, user)  # init a null quiz result
                quizData = str(request.POST.get('quizString').encode('ascii','ignore'))
                user_quizresult.collectQuizData(quizData)
            return HttpResponseRedirect('quiz/complete/') # redirect to a thank you page or something
    else: # else user needs to log in
        return HttpResponseRedirect('/login') # redirect to some result page to show the "result"
