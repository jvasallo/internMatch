from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login
from register.forms import InternRegistrationForm, CompanyRegistrationForm
from django.contrib.contenttypes.models import ContentType
from register.models import Profile

# Uncomment to debug in terminal


def InternRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    if request.method == 'POST':
        form = InternRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'],)
            import pdb; pdb.set_trace()
            user.save()
            profile           = user.get_profile()
            profile.name      = form.cleaned_data['name']
            profile.school    = form.cleaned_data['school']
            #import pdb; pdb.set_trace()
            profile.graduation_date = form.cleaned_data['graduation_date']
            profile.major     = form.cleaned_data['major']
            profile.is_intern = True           
            profile.save()
            return HttpResponseRedirect('/register/quiz')
        else:
            #import pdb; pdb.set_trace()
            return render_to_response('intern_registration.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = InternRegistrationForm()
        context = {'form': form}
        return render_to_response('intern_registration.html', context, context_instance=RequestContext(request))
    
def CompanyRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'],)
            #import pdb; pdb.set_trace()
            user.save()
            login(request, user)
            company           = user.get_profile()
            company.name      = form.cleaned_data['name']
            company.is_intern = False
            #import pdb; pdb.set_trace()
            company.save()
            return HttpResponseRedirect('/register/quiz')
        else:
            #import pdb; pdb.set_trace()
            return render_to_response('intern_registration.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = CompanyRegistrationForm()
        context = {'form': form}
        return render_to_response('intern_registration.html', context, context_instance=RequestContext(request))
    
def Signin(request):
    import pdb; pdb.set_trace()
    #user = authenticate(username='1', password='password') GET PASSWORD FROM FORM AND AUTHENTICATE
    #login(request, user)
    profile = Profile.objects.get(user_id=user.id)
    if request.method == 'GET':
        
        if request.user.is_authenticated() and profile.is_intern:
            return HttpResponseRedirect('/profile/intern')
        if request.user.is_authenticated() and not profile.is_intern:
            return HttpResponseRedirect('/profile/company')
    
    
def QuizResultsParsing(request):
    import pdb; pdb.set_trace()
    if request.user.is_authenticated(): # if user is logged in https://docs.djangoproject.com/en/dev/topics/forms/?from=olddocs
        if request.method == 'POST': # and if request is a POST
            q = Quiz.create(request.user.user_id)  # init a null quiz result
        if form.is_valid():  # if the form passes all the validations
            q.collectQuizData(request.POST) # use the request to sent the data to the def collectQuizData
        return HttpResponseRedirect('/thankyou') # redirect to a thank you page or something
    else: # else user needs to log in
        return HttpResponseRedirect('../../user/profile')
        #return render_to_response('intern_registration.html', context, context_instance=RequestContext(request)) # redirect them back to the registration page or error page.
