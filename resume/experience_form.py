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

        self.helper.layout = Layout(Fieldset('Enter any course projects or work related experiences',
                                             Field('title'),
                                             Field('company_class_name'),
                                             Field('start_date', css_class='date'),
                                             Field('end_date', css_class='date'),
                                             Field('city'),
                                             Field('state'),
                                             Field('description'),
                                             css_class='fields'),
                                    ButtonHolder(Button('button', 'Add Another Experience', css_class='btn btn-large btn-primary add-experience')),
                                    )
        super(ResumeForm, self).__init__(*args, **kwargs)
 
    title = forms.CharField(label=(u'Project/Job Title'), required=False,)
    company_class_name = forms.CharField(label=(u'Course/Company Name'), required=False,)
    start_date = forms.DateField(label=(u'Start Date'), required=True,)
    end_date = forms.DateField(label=(u'End Date'), required=False,)
    city = forms.CharField(label=(u'City'), required=False,)
    state = forms.CharField(label=(u'State'), required=False,)
    description = forms.CharField(label=(u'Job Description'), required=True,)
    
    def clean(self):
        return self.cleaned_data
