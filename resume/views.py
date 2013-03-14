from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from resume.forms import ReferenceForm
from resume.models import Reference
from datetime import date

def ReferencePosting(request):
    if request.user.is_authenticated():
        user = request.user
        profile = user.get_profile()
        if not profile.is_intern:
            return HttpResponseRedirect('/profile')
        form = ReferenceForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                reference_post = add_reference(form, profile)
                return HttpResponseRedirect('/profile')
            else:
                return render_to_response('resume/reference_post.html', {'form': form, 'userProfile' : profile}, context_instance=RequestContext(request))
        else:
            form = ReferenceForm()
            return render_to_response('resume/reference_post.html', {'form': form, 'userProfile' : profile}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/register/intern')

def edit(request, reference_id):
    try:
        reference = Reference.objects.get(pk=reference_id)
    except JobPost.DoesNotExist:
        raise Http404
    if request.user.is_authenticated():
        user = request.user
        userProfile = request.user.get_profile()
        if userProfile.is_intern:
            context = {'user': user, 'userProfile': userProfile, 'reference' : reference}
            return render_to_response('resume/reference_edit.html', context, context_instance=RequestContext(request))
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
                reference = Reference.objects.get(pk=request.POST.get('id'))
            except Reference.DoesNotExist:
                raise Http404
            if profile.is_intern:
                reference.name = request.POST.get('name')
                reference.relationship = request.POST.get('relationship')
                reference.email = request.POST.get('email')
                reference.save()
            return redirect('/profile/references')
    else: # else user needs to log in
        return HttpResponseRedirect('/login') # redirect to some result page to show the "result"

def delete(request, reference_id):
    try:
        reference = Reference.objects.get(pk=reference_id)
    except Reference.DoesNotExist:
        raise Http404
    if request.user.is_authenticated():
       if reference.profile == request.user.get_profile():
           reference.delete()
           return HttpResponseRedirect('/profile/references')
       else:
           return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login')

def add_reference(form, profile):
    reference = Reference()
    reference.profile = profile
    reference.name = form.cleaned_data['name']
    reference.relationship = form.cleaned_data['relationship']
    reference.email = form.cleaned_data['email']
    reference.save()
    return reference
