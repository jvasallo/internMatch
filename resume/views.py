from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from job_post.forms import JobPostForm
from job_post.models import Skill
from datetime import date

def ResumePosting(request):
    if request.user.is_authenticated():
        profile = request.user.get_profile()
        if not profile.is_intern:
            return HttpResponseRedirect('/profile')
        form = ResumePostForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                resume_post = add_resume(form, profile)
                add_skill(request.POST.getlist('main_skills'), resume_post, 'required')
                add_skill(request.POST.getlist('secondary_skills'), resume_post, 'desired')
                return HttpResponseRedirect('/profile')
            else:
                return render_to_response('resume/resume-form.html', {'form': form}, context_instance=RequestContext(request))
        else:
            form = ResumePostForm()
            return render_to_response('resume/resume-form.html', {'form': form}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/register/intern')

#def detail(request, resume_post_id):
#    try:
#        resumepost = JobPost.objects.get(pk=resume_post_id)
#    except JobPost.DoesNotExist:
#        raise Http404
#    return render_to_response('resume-post/detail.html', {'resumepost': resumepost}, context_instance=RequestContext(request))

def add_resume(form, profile):
    resume = ResumePost()
    resume.summary = form.cleaned_data['summary']
    resume.date_post_ends = form.cleaned_data['start_date']
    resume.date_posted = date.today()
    resume_post.position = form.cleaned_data['position']
    resume_post.description = form.cleaned_data['description']
    resume_post.headline = form.cleaned_data['headline']
    resume_post.company_bio = form.cleaned_data['company_bio']
    resume_post.state = form.cleaned_data['state']
    resume_post.city = form.cleaned_data['city']
    resume_post.save()
    return resume_post

def add_skill(skills, resume, type):
    for s in skills:
        skill = Skill()
        skill.name = s
        skill.resume = resume
        skill.type = type
        skill.save()

def add_activity(activities, resume, type):
    for s in skills:
        skill = Skill()
        skill.name = s
        skill.resume = resume
        skill.type = type
        skill.save()

