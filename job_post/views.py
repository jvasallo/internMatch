from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from job_post.forms import JobPostForm
from job_post.models import JobPost, Skill
from datetime import date

# reverse lookup state list...
states = {'Alabama': 'AL',   
        'Alaska': 'AK',   
        'Arizona': 'AZ',   
        'Arkansas': 'AR',   
        'California': 'CA',   
        'Colorado': 'CO',   
        'Connecticut': 'CT',   
        'Delaware': 'DE',   
        'Dist of Columbia': 'DC',   
        'Florida': 'FL',   
        'Georgia': 'GA',   
        'Hawaii': 'HI',   
        'Idaho': 'ID',   
        'Illinois': 'IL',   
        'Indiana': 'IN',
        'Iowa': 'IA',   
        'Kansas':'KS',   
        'Kentucky':'KY',   
        'Louisiana': 'LA',   
        'Maine': 'ME',   
        'Maryland':'MD',   
        'Massachusetts':'MA',    
        'Michigan': 'MI',   
        'Minnesota': 'MN',   
        'Mississippi': 'MS',   
        'Missouri': 'MO',   
        'Montana': 'MT',   
        'Nebraska': 'NE',   
        'Nevada': 'NV',   
        'New Hampshire': 'NH',   
        'New Jersey': 'NJ',   
        'New Mexico': 'NM', 
        'New York': 'NY', 
        'North Carolina': 'NC', 
        'North Dakota': 'ND',   
        'Ohio': 'OH',   
        'Oklahoma': 'OK',   
        'Oregon': 'OR',   
        'Pennsylvania': 'PA',   
        'Rhode Island': 'RI',   
        'South Carolina': 'SC',   
        'South Dakota': 'SD',   
        'Tennessee': 'TN',   
        'Texas': 'TX',   
        'Utah': 'UT',   
        'Vermont': 'VT',   
        'Virginia': 'VA',   
        'Washington': 'WA',   
        'West Virginia': 'WV',   
        'Wisconsin': 'WI',
        'Wyoming': 'WY' }


def JobPosting(request):
    if request.user.is_authenticated():
        user = request.user
        userProfile = request.user.get_profile()
        if userProfile.is_intern:
            return HttpResponseRedirect('/profile')
        form = JobPostForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                job_post = add_job_post(form,userProfile)
                add_skills(request.POST.getlist('desired_skills')[0].split(','), job_post, 'desired')
                add_skills(request.POST.getlist('required_skills')[0].split(','), job_post, 'required')
                return HttpResponseRedirect('/profile/jobs')
            else:
                return render_to_response('job-post/job_post.html', {'user': user, 'userProfile': userProfile, 'form': form}, context_instance=RequestContext(request))
        else:
            form = JobPostForm()
            return render_to_response('job-post/job_post.html', {'user': user, 'userProfile': userProfile, 'form': form}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/register/company')

def detail(request, job_post_id):
    user = None
    userProfile = None
    if request.user.is_authenticated():
	user = request.user
        userProfile = user.get_profile()
    try:
        jobpost = JobPost.objects.get(pk=job_post_id)
    except JobPost.DoesNotExist:
        raise Http404
    context = {'user': user, 'userProfile': userProfile, 'jobpost': jobpost}
    return render_to_response('job-post/job_detail.html', context, context_instance=RequestContext(request))

def add_job_post(form, profile):
    job_post = JobPost()
    job_post.company = profile
    job_post.date_post_ends = form.cleaned_data['date_post_ends']
    job_post.date_posted = date.today()
    job_post.position = form.cleaned_data['position']
    job_post.description = form.cleaned_data['description']
    job_post.headline = form.cleaned_data['headline']
    job_post.company_bio = form.cleaned_data['company_bio']
    job_post.state = form.cleaned_data['state']
    job_post.city = form.cleaned_data['city']
    if form.cleaned_data['url']:
        job_post.url = form.cleaned_data['url']
        job_post.url = job_post.fixUrl()
    job_post.save()
    return job_post

def edit(request, job_post_id):
    try:
        jobpost = JobPost.objects.get(pk=job_post_id)
    except JobPost.DoesNotExist:
        raise Http404
    if request.user.is_authenticated():
        user = request.user
        userProfile = request.user.get_profile()
        if not userProfile.is_intern:
            active =  False if jobpost.date_post_ends < date.today() else True
            context = {'user': user, 'userProfile': userProfile, 'posting' : jobpost, 'active': active}
            return render_to_response('job-post/job_edit.html', context, context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def update(request):
    if request.user.is_authenticated(): # if user is logged in https://docs.djangoproject.com/en/dev/topics/forms/?from=olddocs
        user = request.user
        profile = user.get_profile()
        if request.method == 'POST': # and if request is a POST
            try: # try to get a posting record
                posting = JobPost.objects.get(pk=request.POST.get('id'))
            except JobPost.DoesNotExist:
                raise Http404
            if not profile.is_intern:
                #import pdb; pdb.set_trace()
                posting.headline = request.POST.get('headline')
                posting.position = request.POST.get('position')
                posting.description = request.POST.get('description')
                posting.company_bio = request.POST.get('company_bio')
                posting.city = request.POST.get('city')
                if request.POST.get('state') in states:
                    posting.state = states[request.POST.get('state')]
                posting.date_post_ends = request.POST.get('end_date')
                posting.url = request.POST.get('url')
##                if request.POST.get('url') != '':
##                    posting.url = request.POST.get('url')
##                    posting.url = posting.fixUrl()
                if request.POST.get('desired') != posting.getDesSkillList():
                    posting.skill_set.filter(type='desired').delete()
                    add_skills(request.POST.getlist('desired')[0].split(','), posting, 'desired')
                if request.POST.get('required') != posting.getReqSkillList():
                    posting.skill_set.filter(type='required').delete()
                    add_skills(request.POST.getlist('required')[0].split(','), posting, 'required')
                posting.save()
            return redirect('/profile/jobs')
    else: # else user needs to log in
        return HttpResponseRedirect('/login') # redirect to some result page to show the "result"

def deletePost(request, job_post_id):
    try:
        jobpost = JobPost.objects.get(pk=job_post_id)
    except JobPost.DoesNotExist:
        raise Http404
    if request.user.is_authenticated():
       if jobpost.company.id == request.user.id:
           jobpost.delete()
           return HttpResponseRedirect('/profile/jobs')
       else:
           return HttpResponseRedirect('/') 
    else:
        return HttpResponseRedirect('/login')

def add_skills(skills, job_post, type):
    for s in skills:
        if(len(s)):
            skill = Skill()
            skill.name = s
            skill.job_post = job_post
            skill.type = type
            skill.save()
