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

        self.helper.layout = Layout(Fieldset('Enter any references',
                                             Field('name'),
                                             Field('relationship'),
                                             Field('email'),
                                    ButtonHolder(Button('button', 'Add Another Reference', css_class='btn btn-large btn-primary add-reference')),
                                    ButtonHolder(Submit('submit', 'Save', css_class='btn btn-large btn-primary'))
                                    )
        super(ResumeForm, self).__init__(*args, **kwargs)
 
    name = forms.CharField(label=(u'Reference Name'), required=False,)
    relationship = forms.CharField(label=(u'Relationship to Reference'), required=False,)
    email = forms.CharField(label=(u'Contact E-Mail'), required=False,)
    
    def clean(self):
        return self.cleaned_data
