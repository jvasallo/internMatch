from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from job_post.forms import JobPostForm
from job_post.models import JobPost, Skill
from datetime import date

def JobPosting(request):
    if request.user.is_authenticated():
        profile = request.user.get_profile()
        if profile.is_intern:
            return HttpResponseRedirect('/profile')
        form = JobPostForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                job_post = add_job_post(form,profile)
                #import pdb; pdb.set_trace()
                add_skill(request.POST.getlist('desired_skills'), job_post, 'desired')
                add_skill(request.POST.getlist('required_skills'), job_post, 'required')
                                    
                return HttpResponseRedirect('/profile')
        else:
            form = JobPostForm()
            return render_to_response('job-post.html', {'form': form}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/register/company')

def add_job_post(form, profile):
    job_post = JobPost()
    job_post.company = profile
    job_post.date_post_ends = form.cleaned_data['date_post_ends']
    job_post.date_posted = date.today()
    job_post.description = form.cleaned_data['description']
    job_post.headline = form.cleaned_data['headline']
    job_post.company_bio = form.cleaned_data['company_bio']
    job_post.state = form.cleaned_data['state']
    job_post.city = form.cleaned_data['city']
    job_post.save()
    return job_post

def add_skill(skills, job_post, type):
    for s in skills:
        skill = Skill()
        skill.name = s
        skill.job_post = job_post
        skill.type = type
        skill.save()
