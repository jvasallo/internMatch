from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML

class SigninForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-signin'
        self.helper.form_class = 'form-signin'
        self.helper.form_method = 'post'
        self.helper.form_action = '/login'
        self.helper.layout = Layout(
                                    HTML("""<h2 class="form-signin-heading">Sign In</h2>"""),
                                    Fieldset(
                                                HTML("""<h2 class="form-signin-heading">Please sign in</h2>"""),
                                                'username',
                                                'password',
                                    ),
									#HTML("""<a href="{% url password_reset %}">Forgot password?</a>"""), 
                                    ButtonHolder(Submit('submit', 'Sign In', css_class='btn btn-medium btn-primary')),
                                    HTML("""
                                         <div class="row">
                                            <div class="span4">
                                                <br>
                                                <a href="{% url password_reset %}">Forgot password?</a><br>
                                                <br>
                                                Not registered? Sign up today as a: 
                                                <br>  
                                                <a href="/register/company">Company</a> or <a href="/register/intern">Intern</a>
                                            </div>
                                         </div> """),
                                    )
        super(SigninForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(label=(u'User Name'), required=True)
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False), required=True,
                               min_length=6
                              )

    
    class Meta:
        exclude = ('user',)
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user == None:
            raise forms.ValidationError("Invalid login")        
        return self.cleaned_data
