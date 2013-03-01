from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from quiz.models import QuizResult
from job_post.models import JobPost

def index(request):
    if request.user.is_authenticated():
        user = request.user
        userProfile = request.user.get_profile()
        if userProfile.is_intern:
            try:
                postingList = JobPost.objects.all()
                postings = []
                for eachPosting in postingList:
                    if eachPosting.company.quizResult() == userProfile.quizResult():
                        postings.append(eachPosting)
            except Exception:
                postings = None 
            return render_to_response('search/job_search.html', {'user': user, 'userProfile' : userProfile, 'postings': postings}, context_instance=RequestContext(request))
        else:
            try:
                userList = User.objects.all()
                userProfileList = []
                interns = []
                for eachUser in userList:
                    userProfileList.append(eachUser.get_profile())
                for eachProfile in userProfileList:
                    if eachProfile.is_intern and eachProfile.quizResult() == userProfile.quizResult():
                        interns.append(eachProfile)
            except Exception:
                interns = None
            return render_to_response('search/intern_search.html', {'user': user, 'userProfile' : userProfile, 'interns' : interns}, context_instance=RequestContext(request))
    else:
        postings = JobPost.objects.all()
        return render_to_response('search/job_search.html', {'user': None, 'postings': postings}, context_instance=RequestContext(request))
