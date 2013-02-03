from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from register.models import Intern
from crispy_forms.helper import FormHelper

class RegistrationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        super(RegistrationForm, self).__init__(*args, **kwargs)
    
    MAJORS = (
    ('1', 'Accountancy'),
    ('2', 'Business Administration'),
    ('3', 'Computer Science'),
    ('4', 'Finance'),
    ('5', 'Information Technology'),
    ('6', 'Mathematics'),
    )
    
    STATES = (
    ('1', 'Alabama'),
    ('2', 'Alaska'),
    ('3', 'Arizona'),
    ('4', 'Arkansas'),
    ('5', 'California'),
    )

    name             = forms.CharField(label=(u'Name'))
    address          = forms.CharField(label=(u'Address'))
    city             = forms.CharField(label=(u'City'))
    state            = forms.ChoiceField(label=(u'State'), choices=STATES)
    zip              = forms.CharField(label=(u'Zip'))
    school           = forms.CharField(label=(u'School'))
    graduation_date  = forms.DateField(label=(u'Graduation Date'))   
    major            = forms.ChoiceField(label=(u'Major'), choices=MAJORS)
    username         = forms.CharField(label=(u'User Name'))
    email            = forms.EmailField(label=(u'Email Address'))
    password         = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1        = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
    
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
        self.cleaned_data['graduation_date']
        import pdb; pdb.set_trace()
        return self.cleaned_data
    
    def clean_graduation(self):
        import pdb; pdb.set_trace()
        return self.cleaned_data['graduation_date']