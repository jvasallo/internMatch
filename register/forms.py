from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from register.models import Intern
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class InternRegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Sign up'))
        super(InternRegistrationForm, self).__init__(*args, **kwargs)
    
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

    name             = forms.CharField(
                                       label=(u'Name'),
                                       required=True,
                                       )
    school           = forms.CharField(
                                       label=(u'School'),
                                       required=True,
                                       )
    graduation_date  = forms.DateField(
                                       label=(u'Graduation Date'),
                                       required=True,
                                       )   
    major            = forms.ChoiceField(
                                         label=(u'Major'),
                                         choices=MAJORS,
                                         required=True,
                                          )
    username         = forms.CharField(
                                       label=(u'User Name'),
                                       required=True,
                                       )
    email            = forms.EmailField(
                                        label=(u'Email Address'),
                                        required=True,
                                        )
    password         = forms.CharField(
                                       label=(u'Password'),
                                       widget=forms.PasswordInput(render_value=False),
                                       required=True,
                                       min_length=6,
                                       )
    password1        = forms.CharField(
                                       label=(u'Verify Password'),
                                       widget=forms.PasswordInput(render_value=False),
                                       required=True,
                                       min_length=6,
                                       )
    
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
        
        #import pdb; pdb.set_trace()
        return self.cleaned_data
    
    def clean_graduation(self):
        #import pdb; pdb.set_trace()
        return self.cleaned_data['graduation_date']
    
    

class CompanyRegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Sign up'))
        super(CompanyRegistrationForm, self).__init__(*args, **kwargs)
    

    
    STATES = (
    ('1', 'Alabama'),
    ('2', 'Alaska'),
    ('3', 'Arizona'),
    ('4', 'Arkansas'),
    ('5', 'California'),
    )

    name             = forms.CharField(
                                       label=(u'Name'),
                                       required=True,
                                       )
#    school           = forms.CharField(
#                                       label=(u'School'),
#                                       required=True,
#                                       )
#    graduation_date  = forms.DateField(
#                                       label=(u'Graduation Date'),
#                                       required=True,
#                                       )   
#    major            = forms.ChoiceField(
#                                         label=(u'Major'),
#                                         choices=MAJORS,
#                                         required=True,
#                                          )
    username         = forms.CharField(
                                       label=(u'User Name'),
                                       required=True,
                                       )
    email            = forms.EmailField(
                                        label=(u'Email Address'),
                                        required=True,
                                        )
    password         = forms.CharField(
                                       label=(u'Password'),
                                       widget=forms.PasswordInput(render_value=False),
                                       required=True,
                                       min_length=6,
                                       )
    password1        = forms.CharField(
                                       label=(u'Verify Password'),
                                       widget=forms.PasswordInput(render_value=False),
                                       required=True,
                                       min_length=6,
                                       )
    
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
        
        #import pdb; pdb.set_trace()
        return self.cleaned_data