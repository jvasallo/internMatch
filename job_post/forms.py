from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from register.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Field, MultiField, Button
    
class JobPostForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal job-posting'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout(
                                    HTML("""<h2 class="form-job-post-heading">Job Posting</h2>"""),
                                    Fieldset(
                                             'Enter relevant information',
                                             Field('headline'),
                                             Field('position'),
                                             Field('description'),
                                             Field('date_post_ends', css_class='date'),
                                             Field('company_bio'),
                                             Field('required_skills'),
                                             Field('desired_skills'),
                                             Field('city'),
                                             Field('state'),
                                             ButtonHolder(Button('button', 'Add Required Skill', css_class='btn btn-large btn-primary add-req-skill')),
                                             ButtonHolder(Button('button', 'Add Desired Skill', css_class='btn btn-large btn-primary add-des-skill')),
                                             css_class='fields'
                                    ),
                                    ButtonHolder(Submit('submit', 'Save', css_class='btn btn-large btn-primary'))
                                    )
        super(JobPostForm, self).__init__(*args, **kwargs)
 

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
