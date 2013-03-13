from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
from django.template import RequestContext
from quiz.models import QuizResult
from job_post.models import JobPost
from datetime import date
from django.db.models import Q


# Filter the search request by intern or company, passing along any GET parameters
def router(request):
#    import pdb; pdb.set_trace()
    response = redirect('/search/intern')
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        if not user_profile.is_intern:
            response = redirect('search/company')
    get_params = '?keyword=' + request.GET.get('keyword','') + '&location=' + request.GET.get('location','') + '&page=' + request.GET.get('page','1')
    response['Location'] += get_params
    return response

#def getGetParams(request):
#    result = '?'
#    for key,value in request.GET.iteritems():
#        result += key + '=' + value + '&'
    
    
# intern or anonomous user search results
def intern(request):
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        if not user_profile.is_intern:
            return redirect('search/company')
    keyword = request.GET.get('keyword',False)
    location = request.GET.get('location',False)
    search_terms = {'keyword': keyword, 'location': location}
    page = request.GET.get('page',False)
    postings = []
#    import pdb; pdb.set_trace()
    posting_list = getPostingsFromKeyword(keyword)
    posting_list = getPostingsFromLocation(posting_list,location)
    posting_list = getPostingsByPage(posting_list,page)
#    JobPost.objects.all().order_by('date_post_ends')[k:n]
    for posting in posting_list:
        posting_company = User.objects.get(id=posting.company.id)
        if posting_company.is_active:
            postings.append(posting)
    if request.user.is_authenticated(): 
        context = {'user': request.user, 'userProfile' : user_profile, 'postings': postings, 'search_terms': search_terms}
    else:
        context = {'user': None, 'postings': postings, 'search_terms':search_terms}
    return render_to_response('search/job_search.html', context, context_instance=RequestContext(request))
    
def getPostingsFromLocation(posting_list,location):
#    import pdb; pdb.set_trace()
    if posting_list and location:
        return posting_list.filter(city__contains=location).distinct().filter(date_post_ends__gte=date.today()).order_by('date_post_ends') | posting_list.filter(state__contains=location).distinct().filter(date_post_ends__gte=date.today()).order_by('date_post_ends')
    return posting_list
        
        
    
# Get postings by page(assume ordered by date), 5 postings per page
def getPostingsByPage(postings, page):
    per_page = 5
    if page:
        page = int(page) - 1
        slice = per_page*page
        return postings[slice:slice+per_page]
    return postings[:per_page]

def getPostingsFromKeyword(keyword):
    if keyword:
        return JobPost.objects.filter(skill__name__contains=keyword).distinct().filter(date_post_ends__gte=date.today()).order_by('date_post_ends')
    return JobPost.objects.filter(date_post_ends__gte=date.today()).distinct().order_by('date_post_ends')


def index(request):
#    import pdb; pdb.set_trace()
    if request.method == 'GET':
        keyword = request.GET.get('keyword',False)
        location = request.GET.get('location',False)
        search_terms = {'keyword': keyword, 'location': location}
#        import pdb; pdb.set_trace()
        
        if request.user.is_authenticated():
            user = request.user
            userProfile = request.user.get_profile()
            if userProfile.is_intern:
                try:
                    posting_list = getPostingsFromKeyword(keyword)
                    posting_list = getPostingsByPage(page)
                    postings = []
                    for eachPosting in posting_list:
                        try:
                            postingCompany = User.objects.get(id=eachPosting.company.id)
                            if postingCompany.is_active:# and eachPosting.company.quizResult() == userProfile.quizResult():
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
            postingList = JobPost.objects.filter(skill__name__contains=keyword).distinct().filter(date_post_ends__gte=date.today())
            postings = []
            for eachPosting in postingList:
                try:
                    postingCompany = User.objects.get(id=eachPosting.company.id)
                    if postingCompany.is_active:
                        postings.append(eachPosting)        
                except Exception:
                    print 'skip'
            return render_to_response('search/job_search.html', {'user': None, 'postings': postings, 'search_terms':search_terms}, context_instance=RequestContext(request))
        