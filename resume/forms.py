from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from register.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Field, MultiField, Button, Div
    
class ReferenceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal resume'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout(Div(
                                    HTML("""<h2 class="form-job-post-heading">Add Reference Form</h2>"""),
                                    Fieldset(
                                             'Enter relevant information',
                                             Field('name'),
                                             Field('relationship'),
                                             Field('email'),
                                             css_class='fields'
                                    ),
                                    ButtonHolder(Submit('submit', 'Save', css_class='btn btn-large btn-primary')),
				    css_class="span10")
                                    )
        super(ReferenceForm, self).__init__(*args, **kwargs)
 
    name = forms.CharField(label=('Name'), required=False,)
    relationship = forms.CharField(label=('Relationship'), required=False,)
    email = forms.CharField(label=('E-Mail'), required=False,)
    
    def clean(self):
        return self.cleaned_data
