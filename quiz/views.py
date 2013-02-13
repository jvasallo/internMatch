from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from quiz.models import Quiz

def QuizResultsParsing(request):
    import pdb; pdb.set_trace()
    if request.user.is_authenticated(): # if user is logged in https://docs.djangoproject.com/en/dev/topics/forms/?from=olddocs
	if request.method == 'POST': # and if request is a POST
            q = Quiz.create(request.user.user_id)  # init a null quiz result
	    if form.is_valid():  # if the form passes all the validations
                q.collectQuizData(request.POST) # use the request to sent the data to the def collectQuizData
        return HttpResponseRedirect('/thankyou') # redirect to a thank you page or something
    else: # else user needs to log in
        form = RegistrationForm() 
        context = {'form': form}
        return render_to_response('intern_registration.html', context, context_instance=RequestContext(request)) # redirect them back to the registration page or error page.
