from datetime import date

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from job_post.models import JobPost
from register.models import Profile

import math

POSTINGS_PER_PAGE = 5

# Filter the search request by intern or company, passing along any GET parameters
def router(request):
    # import pdb; pdb.set_trace()
    response = redirect('/search/intern')
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        if not user_profile.is_intern:
            response = redirect('/search/company')
    page = request.GET.get('page', 1) if int(request.GET.get('page', 1)) > 1 else 1
    get_params = '?keyword=' + request.GET.get('keyword', '') + '&location=' + request.GET.get('location',
                                                                                               '') + '&personality_filter=' + request.GET.get(
        'personality_filter', '') + '&page=' + unicode(page)
    response['Location'] += get_params
    return response

# intern or anonymous user search results
def intern(request):
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        if not user_profile.is_intern:
            return redirect('search/company')
    keyword = request.GET.get('keyword', False)
    personality_filter = request.GET.get('personality_filter', 'off')
    location = request.GET.get('location', False)
    page = request.GET.get('page', False)
    get_params = {'location': location, 'page': int(page), 'personality_filter': personality_filter, 'keyword': keyword}
    posting_list = getPostingsFromKeyword(keyword)
    for l in location.split(' '):
        posting_list = getPostingsFromLocation(posting_list, l.strip(','))

    if request.user.is_authenticated():
        quiz = user_profile.quizResult()
        if personality_filter == 'on' and user_profile.quizResult():
            posting_list = getPostingsFromPersonality(quiz, posting_list)
            quiz = True
        pagination = getPagination(int(page),len(posting_list))
        postings = getListingsByPage(posting_list, page)
        context = {'user': request.user, 'userProfile': user_profile, 'get_params': get_params,
                   'personality_filter': personality_filter, 'postings': postings, 'quiz': quiz,
                   'postings_per_page': POSTINGS_PER_PAGE, 'pagination': pagination}
    else:
        pagination = getPagination(int(page),len(posting_list))
        postings = getListingsByPage(posting_list, page)
        context = {'user': None, 'postings': postings, 'get_params': get_params,
                   'personality_filter': personality_filter,'postings_per_page': POSTINGS_PER_PAGE,
                   'pagination': pagination}
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
        get_params = {'location': location, 'page': page, 'personality_filter': personality_filter, 'keyword': keyword}

        interns = False
        for k in keyword.split(' '):
            interns = getInternsFromKeyword(k.strip(','), interns)
        for l in location.split(' '):
            interns = getInternsFromLocation(l.strip(','), interns)
        quiz = user_profile.quizResult()
        if personality_filter == 'on' and user_profile.quizResult():
            interns = getInternsFromPersonality(quiz, interns)
            quiz = True
        pagination = getPagination(int(page),len(interns))
        interns = getListingsByPage(interns, page)
        context = {'user': request.user, 'userProfile': user_profile, 'interns': interns, 'get_params': get_params,
                   'personality_filter': personality_filter, 'postings_per_page': POSTINGS_PER_PAGE, 'pagination': pagination, 'quiz': quiz}
        return render_to_response('search/intern_search.html',context, context_instance=RequestContext(request))

# Determine which pagination numbers to display
def getPagination(page, total_listings):
    pages_to_display = 4
    result = [i for i in range(1,int(math.ceil(float(total_listings)/POSTINGS_PER_PAGE)) + 1)]
    if len(result) <= pages_to_display:
        return {'pages': result, 'left_page': False, 'right_page': False}
    if pages_to_display - result[page - 1] < 0:
        result = result[len(result) - pages_to_display:]
        return {'pages': result, 'left_page': result[0] - pages_to_display, 'right_page': False}
    if page <= pages_to_display:
        result = result[:pages_to_display]
        return {'pages': result, 'left_page': False, 'right_page': pages_to_display + 1}
    result = result[page-1:]
    return {'pages': result, 'left_page': result[0] - pages_to_display, 'right_page': result[0] + pages_to_display}

def getInternsFromPersonality(quiz_result, interns=False):
    result = Profile.objects.filter(is_intern=True).filter(user__is_active=True).filter(name__isnull=False).distinct()
    if quiz_result:
        result = Profile.objects.filter(is_intern=True).filter(user__quizresult__quiz_result=quiz_result).distinct()
    if interns != False:
        result = (result & interns).distinct()
    return result


def getPostingsFromPersonality(quiz_result, postings=False):
    result = JobPost.objects.filter(date_post_ends__gte=date.today()).order_by('date_post_ends').distinct()
    if quiz_result:
        result = JobPost.objects.filter(company__user__quizresult__quiz_result=quiz_result).distinct()
    if postings != False:
        result = (result & postings).distinct()
    return result


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
    if page:
        page = int(page) - 1
        num_listings = POSTINGS_PER_PAGE * page
        return listings[num_listings: num_listings + POSTINGS_PER_PAGE]
    return listings[:POSTINGS_PER_PAGE]


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
