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
                                    )
        super(ResumeForm, self).__init__(*args, **kwargs)
 

    summary = forms.CharField(label=(u'Professional Summary'), required=True,)
    skills = forms.CharField(label=(u'Skill'), required=False,)
    activities = forms.CharField(label=(u'Activity'), required=False,)
    
    def clean(self):
        return self.cleaned_data
