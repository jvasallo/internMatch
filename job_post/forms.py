from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from register.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Field, MultiField, Button, Div
    
class JobPostForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal row job-posting'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout(Div(
                                    HTML("""<h2 class="form-job-post-heading">Job Posting</h2>"""),
                                    Fieldset(
                                             'Enter relevant information',
                                             Field('headline'),
                                             Field('position'),
                                             Field('description'),
                                             Field('company_bio'),
                                             Field('required_skills'),
                                             Field('desired_skills'),
                                             Field('city'),
                                             Field('state'),
                                             Field('date_post_ends', css_class='date'),
                                             css_class='fields'
                                    ),
                                    ButtonHolder(Submit('submit', 'Save', css_class='btn btn-large btn-primary')),css_class="span10")
                                    )
        super(JobPostForm, self).__init__(*args, **kwargs)
 

    headline        = forms.CharField(
                                               label=(u'Job Posting Headline'),
                                               widget=forms.TextInput(attrs={'class':'span6'}),
                                               required=True,)
    description     = forms.CharField(
                                               label=(u'Job Description'),
                                               widget=forms.Textarea(attrs={'class':'span6'}),
                                               required=True,
                                               )
    date_post_ends  = forms.DateField(
                                               label=(u'Date posting will end'),
                                               widget=forms.TextInput(attrs={'class':'span6'}),
                                               required=True,)
    position        = forms.CharField(          
                                               label=(u'Position'),
                                               widget=forms.TextInput(attrs={'class':'span6'}),
                                               required=True,)
    required_skills = forms.CharField(
                                               label=(u'Required Skills - Enter a comma separated list'),
                                               widget=forms.Textarea(attrs={'class':'span6'}),
                                               required=False,)
    desired_skills  = forms.CharField(         
                                               label=(u'Desired Skills - Enter a comma separated list'),
                                               widget=forms.Textarea(attrs={'class':'span6'}),
                                               required=False,)
    company_bio     = forms.CharField(          
                                               label=(u'Company Bio'),
                                               widget=forms.Textarea(attrs={'class':'span6'}),
                                               required=False,)
    city            = forms.CharField(          
                                               label=(u'City'),
                                               widget=forms.TextInput(attrs={'class':'span6'}),
                                               required=False,)
    state           = forms.CharField(          
                                               label=(u'State'),
                                               widget=forms.TextInput(attrs={'class':'span6'}),
                                               required=False,)
    url             = forms.URLField(          label=(u'Company application url'),
                                               widget=forms.TextInput(attrs={'class':'span6'}),
                                               required=False)
        
    
    def clean(self):
        return self.cleaned_data
