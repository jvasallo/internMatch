from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from register.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Field, MultiField, Button
    
class ResumeFormm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal resume'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout(HTML("""<h2 class="form-resume-heading">Post your Resume</h2>"""),
                                    Fieldset('Enter relevant information',
                                             Field('summary'),
                                             Field('skills'),
                                             Field('activities'),
                                             css_class='fields'),
                                    ButtonHolder(Button('button', 'Add Another Skill', css_class='btn btn-large btn-primary add-skill')),
                                    ButtonHolder(Button('button', 'Add Another Activity', css_class='btn btn-large btn-primary add-activity')),
                                    Fieldset('Enter any course projects or work related experiences',
                                             Field('title'),
                                             Field('company_class_name'),
                                             Field('start_date', css_class='date'),
                                             Field('end_date', css_class='date'),
                                             Field('city'),
                                             Field('state'),
                                             Field('description'),
                                             css_class='fields'),
                                    ButtonHolder(Button('button', 'Add Another Experience', css_class='btn btn-large btn-primary add-experience')),
                                    Fieldset('Enter any references',
                                             Field('name'),
                                             Field('email'),
                                    ButtonHolder(Button('button', 'Add Another Reference', css_class='btn btn-large btn-primary add-reference')),
                                    ButtonHolder(Submit('submit', 'Save', css_class='btn btn-large btn-primary'))
                                    )
        super(ResumeForm, self).__init__(*args, **kwargs)
 

    summary = forms.CharField(label=(u'Professional Summary'), required=True,)
    skills = forms.CharField(label=(u'Skill'), required=False,)
    activities = forms.CharField(label=(u'Activity'), required=False,)
    title = forms.CharField(label=(u'Course/Job Title'), required=False,)
    city = forms.CharField(label=(u'City'), required=False,)
    state = forms.CharField(label=(u'State'), required=False,)
        headline        = forms.CharField(
                                               label=(u'Job Posting Headline'),
                                               required=True,)
    description     = forms.CharField(
                                               label=(u'Job Description'),
                                               required=True,)
    date_post_ends  = forms.DateField(
                                               label=(u'Date posting will end'),
                                               required=True,)
    position           = forms.CharField(
                                               label=(u'Position'),
                                               required=True,)
    required_skills = forms.CharField(
                                               label=(u'Required Skills'),
                                               required=False,)
    desired_skills  = forms.CharField(
                                               label=(u'Desired Skills'),
                                               required=False,)
    company_bio     = forms.CharField(
                                               label=(u'Company Bio'),
                                               required=False,)
    city            = forms.CharField(
                                               label=(u'City'),
                                               required=False,)
    state           = forms.CharField(
                                               label=(u'State'),
                                               required=False,)
    
    
    def clean(self):
        return self.cleaned_data
