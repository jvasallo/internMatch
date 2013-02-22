from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from register.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Field, MultiField
    
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
                                             Field('description'),
                                             Field('date_post_ends', css_class='date'),
                                             Field('skills'),
                                    ),
                                    ButtonHolder(
                                                 Submit('submit', 'Sign In', css_class='btn btn-large btn-primary')
                                                 )
                                    )
        super(JobPostForm, self).__init__(*args, **kwargs)
 

    headline       = forms.CharField(
                                               label=(u'Job Posting Title'),
                                               required=True,)
    description    = forms.CharField(
                                               label=(u'Job Description'),
                                               required=True,)
    date_post_ends = forms.DateField(
                                               label=(u'Date posting will end'),
                                               required=True,)
    skills         = forms.CharField(label=(u'Skills'),required=False,)
        
    
    def clean(self):
        return self.cleaned_data
