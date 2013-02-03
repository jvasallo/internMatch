from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from register.forms import RegistrationForm

# Uncomment to debug in terminal


def InternRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        import pdb; pdb.set_trace()
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'])
            user.save()
            intern = user.get_profile()
            intern.name = form.cleaned_data['name']
            intern.save()
            return HttpResponseRedirect('/profile')
        else:
            import pdb; pdb.set_trace()
            return render_to_response('intern_registration.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('intern_registration.html', context, context_instance=RequestContext(request))
    