from datetime import date

from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.template import RequestContext

from job_post.models import JobPost
from quiz.models import Quiz
from register.models import Profile

# Filter the search request by intern or company, passing along any GET parameters
def router(request):
#    import pdb; pdb.set_trace()
    response = redirect('/search/intern')
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        if not user_profile.is_intern:
            response = redirect('/search/company')
    get_params = '?keyword=' + request.GET.get('keyword', '') + '&location=' + request.GET.get('location',
                                                                                               '') + '&personality_filter=' + request.GET.get(
        'personality_filter', '') + '&page=' + request.GET.get('page', '1')
    response['Location'] += get_params
    return response

# intern or anonomous user search results
def intern(request):
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        if not user_profile.is_intern:
            return redirect('search/company')
    keyword = request.GET.get('keyword', False)
    personality_filter = request.GET.get('personality_filter', 'off')
    location = request.GET.get('location', False)
    page = request.GET.get('page', False)
    get_params = {'location': location, 'page': page, 'personality_filter': personality_filter, 'keyword': keyword}
    postings = []
    posting_list = getPostingsFromKeyword(keyword)
    for l in location.split(' '):
        posting_list = getPostingsFromLocation(posting_list, l.strip(','))
    posting_list = getListingsByPage(posting_list, page)
    for posting in posting_list:
        posting_company = User.objects.get(id=posting.company.id)
        if posting_company.is_active:
            postings.append(posting)
    if request.user.is_authenticated():
        context = {'user': request.user, 'userProfile': user_profile, 'get_params': get_params,
                   'personality_filter': personality_filter, 'postings': postings}
    else:
        context = {'user': None, 'postings': postings, 'get_params': get_params,
                   'personality_filter': personality_filter}
        # import pdb; pdb.set_trace()
    return render_to_response('search/job_search.html', context, context_instance=RequestContext(request))


def company(request):
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        if user_profile.is_intern:
            return redirect('search/intern')
        keyword = request.GET.get('keyword', False)
        personality_filter = request.GET.get('personality_filter', 'off')
        location = request.GET.get('location', False)
        page = request.GET.get('page', False)
        user_profile.q
        quiz_score = Quiz.objects.filter(quiz_result=quizResult)
        get_params = {'location': location, 'page': page, 'personality_filter': personality_filter, 'keyword': keyword}

        interns = False
        for k in keyword.split(' '):
            interns = getInternsFromKeyword(k.strip(','), interns)
        for l in location.split(' '):
            interns = getInternsFromLocation(l.strip(','), interns)
        interns = getListingsByPage(interns, page)

        # import pdb; pdb.set_trace()
        context = {'user': request.user, 'userProfile': user_profile, 'interns': interns, 'get_params': get_params}
        return render_to_response('search/intern_search.html', context, context_instance=RequestContext(request))


def getInternsFromPersonality(keyword, interns=False):
    result = Profile.objects.filter(is_intern=True).filter(user__is_active=True).filter(name__isnull=False).distinct()
    if keyword:
        result = Profile.objects.filter(is_intern=True).filter(skill__name__icontains=keyword).distinct()
    if interns != False:
        result = (result & interns).distinct()
    return result

# def getPostingsFromPersonality(quiz_result, postings=False):
#     result = JobPost.objects.filter(
#     if keyword:
#         result = Profile.objects.filter(is_intern=True).filter(skill__name__icontains=keyword).distinct()
#     if interns != False:
#         result = (result & interns).distinct()
#     return result


def getPostingsFromLocation(posting_list, location):
    if posting_list and location:
        return posting_list.filter(city__icontains=location).distinct().filter(
            date_post_ends__gte=date.today()).order_by('date_post_ends') | posting_list.filter(
            state__icontains=location).distinct().filter(date_post_ends__gte=date.today()).order_by('date_post_ends')
    return posting_list


def getInternsFromKeyword(keyword, interns=False):
    result = Profile.objects.filter(is_intern=True).filter(user__is_active=True).filter(name__isnull=False).distinct()
    if keyword:
        result = Profile.objects.filter(is_intern=True).filter(skill__name__icontains=keyword).distinct()
    if interns != False:
        result = (result & interns).distinct()
    return result


def getInternsFromLocation(location, interns=False):
    result = Profile.objects.filter(is_intern=True).filter(user__is_active=True).filter(name__isnull=False).distinct()
    if location:
        result = Profile.objects.filter(is_intern=True).filter(
            city__icontains=location).distinct() | Profile.objects.filter(is_intern=True).filter(
            state__icontains=location).distinct()
    if interns != False:
        result = (result & interns).distinct()
    return result

# Get listings by page(assume ordered by date), 5 postings per page
def getListingsByPage(listings, page):
    per_page = 5
    if page:
        page = int(page) - 1
        slice = per_page * page
        return listings[slice:slice + per_page]
    return listings[:per_page]


def getPostingsFromKeyword(keyword, postings=False):
    result = JobPost.objects.filter(date_post_ends__gte=date.today()).order_by('date_post_ends').distinct()
    if keyword:
        result = (JobPost.objects.filter(skill__name__icontains=keyword).filter(
            date_post_ends__gte=date.today()).order_by('date_post_ends') | JobPost.objects.filter(
            position__icontains=keyword).filter(
            date_post_ends__gte=date.today()).order_by('date_post_ends') | JobPost.objects.filter(
            headline__icontains=keyword).filter(
            date_post_ends__gte=date.today()).order_by('date_post_ends')).distinct()
    if postings != False:
        result = (result & postings).distinct()
    return result