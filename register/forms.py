from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from register.models import Intern

class RegistrationForm(ModelForm): 
    username    = forms.CharField(label=(u'User Name'))
    email       = forms.EmailField(label=(u'Email Address'))
    password    = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1   = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
    
    class Meta:
        model = Intern
        exclude = ('user',)
        
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Username is already taken")
    
    def clean(self):
        if self.cleaned_data.get("password") != self.cleaned_data.get("password1"):
            raise forms.ValidationError("Passwords did not match")
        return self.cleaned_data