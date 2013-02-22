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
        form = JobPostForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                profile = request.user.get_profile()
                job_post = JobPost()
                job_post.company = profile
                job_post.date_post_ends = form.cleaned_data['date_post_ends']
                job_post.date_posted = date.today()
                job_post.description = form.cleaned_data['description']
                job_post.headline = form.cleaned_data['headline']
                job_post.save()
                
                skills = request.POST.getlist('skills')
                for s in skills:
                    skill = Skill()
                    skill.name = s
                    skill.intern_or_company = profile
                    skill.job_post = job_post
                    skill.save()                
                return HttpResponseRedirect('/profile')
        else:
            return render_to_response('job-post.html', {'form': form}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/register/company')
    