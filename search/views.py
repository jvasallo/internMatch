from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from quiz.models import QuizResult
from job_post.models import JobPost
from datetime import date

#TODO THIS METHOD IS WAAAAAY TO BIG
def index(request):
#    import pdb; pdb.set_trace()
    if request.method == 'GET':
        keyword = request.GET.get('keyword',False)
        location = request.GET.get('location',False)
        search_terms = {'keyword': keyword, 'location': location}
        
        if request.user.is_authenticated():
            user = request.user
            userProfile = request.user.get_profile()
            if userProfile.is_intern:
                try:
                    postings = JobPost.objects.filter(date_post_ends__gte=datetime.date.today())[:1]
                    postingList = JobPost.objects.all()
                    postings = []
                    for eachPosting in postingList:
                        try:
                            postingCompany = User.objects.get(id=eachPosting.company.id)
                            if postingCompany.is_active and eachPosting.company.quizResult() == userProfile.quizResult():
                                postings.append(eachPosting)
                        except Exception:
                            print 'skip'
                except Exception:
                    postings = None
                context = {'user': user, 'userProfile' : userProfile, 'postings': postings, 'search_terms': search_terms}
                return render_to_response('search/job_search.html', context, context_instance=RequestContext(request))
            else:
                try:
                    userList = User.objects.all()
                    userProfileList = []
                    interns = []
                    for eachUser in userList:
                        if eachUser.is_active:
                            userProfileList.append(eachUser.get_profile())
                    for eachProfile in userProfileList:
                        if eachProfile.is_intern and eachProfile.quizResult() == userProfile.quizResult():
                            interns.append(eachProfile)
                except Exception:
                    interns = None
                return render_to_response('search/intern_search.html', {'user': user, 'userProfile' : userProfile, 'interns' : interns, 'search_terms':search_terms}, context_instance=RequestContext(request))
        else:
            postingList = JobPost.objects.all()
            postings = []
            for eachPosting in postingList:
                try:
                    postingCompany = User.objects.get(id=eachPosting.company.id)
                    if postingCompany.is_active:
                        postings.append(eachPosting)        
                except Exception:
                    print 'skip'
            return render_to_response('search/job_search.html', {'user': None, 'postings': postings, 'search_terms':search_terms}, context_instance=RequestContext(request))