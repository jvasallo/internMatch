from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from register.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field

class InternRegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Sign up'))
	super(InternRegistrationForm, self).__init__(*args, **kwargs)

    # Global Variables
    MAJORS = (
    ('', 'Select...'),
    ('Applied Network Systems', 'Applied Network Systems'),
    ('Computer Engineering', 'Computer Engineering'),
    ('Computer Science', 'Computer Science'),
    ('Information Assurance', 'Information Assurance'),
    ('Information Technology', 'Information Technology'),
    ('Project Management', 'Project Management'),
    ('Software Engineering', 'Software Engineering'),
    ('Systems Analysis', 'Systems Analysis'),
    )

    STATUS = (
        ('', 'Select...'),
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Masters Candidate', 'Masters Candidate'),
        ('PhD Candidate', 'PhD Candidate'),
    )
    
    STATES = (
        ('', 'Select...'),
	('AL', 'Alabama'),
	('AK', 'Alaska'),
	('AZ', 'Arizona'),
	('AR', 'Arkansas'),
	('CA', 'California'),
	('CO', 'Colorado'),
	('CT', 'Connecticut'),
	('DE', 'Delaware'),
	('DC', 'Dist of Columbia'),
	('FL', 'Florida'),
	('GA', 'Georgia'),
	('HI', 'Hawaii'),
	('ID', 'Idaho'),
	('IL', 'Illinois'),
	('IN', 'Indiana'),
	('IA', 'Iowa'),
	('KS', 'Kansas'),
	('KY', 'Kentucky'),
	('LA', 'Louisiana'),
	('ME', 'Maine'),
	('MD', 'Maryland'),
	('MA', 'Massachusetts'),
	('MI', 'Michigan'),
	('MN', 'Minnesota'),
	('MS', 'Mississippi'),
	('MO', 'Missouri'),
	('MT', 'Montana'),
	('NE', 'Nebraska'),
	('NV', 'Nevada'),
	('NH', 'New Hampshire'),
	('NJ', 'New Jersey'),
	('NM', 'New Mexico'),
	('NY', 'New York'),
	('NC', 'North Carolina'),
	('ND', 'North Dakota'),
	('OH', 'Ohio'),
	('OK', 'Oklahoma'),
	('OR', 'Oregon'),
	('PA', 'Pennsylvania'),
	('RI', 'Rhode Island'),
	('SC', 'South Carolina'),
	('SD', 'South Dakota'),
	('TN', 'Tennessee'),
	('TX', 'Texas'),
	('UT', 'Utah'),
	('VT', 'Vermont'),
	('VA', 'Virginia'),
	('WA', 'Washington'),
	('WV', 'West Virginia'),
	('WI', 'Wisconsin'),
	('WY', 'Wyoming'),
    )

    name = forms.CharField(label=(u'Name'), required=True)
    school = forms.CharField(label=(u'School'), max_length=80, required=True)
    major = forms.ChoiceField(label=(u'Major'), choices=MAJORS, required=True)
    status = forms.ChoiceField(label=(u'Status'), choices=STATUS, required=True)
    graduation_date = forms.DateField(label=(u'Graduation Date'), required=True)
    city = forms.CharField(label=(u'City'), max_length=22, required=True)
    state = forms.ChoiceField(label=(u'State'), choices=STATES, required=True)
    description = forms.CharField(label=(u'Experience'), widget=forms.Textarea, max_length=1250, required=False)
    username = forms.CharField(label=(u'User Name'), required=True)
    email = forms.EmailField(label=(u'Email Address'), max_length=50, required=True)
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False), required=True, min_length=6)
    password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False), required=True, min_length=6)
    agree_terms = forms.MultipleChoiceField(label = (u'In order to proceed, you must agree with our Terms of Service.'),required=True,
                                                     choices = (('agree', "I have read, and agree to the Terms of Service."),), widget = forms.CheckboxSelectMultiple,
                                                     help_text = "<a href='#termsModal' class='btn btn-mini' type='button' data-toggle='modal'>View Terms of Service</a>")
 
    class Meta:
        model = Profile
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
        return self.cleaned_data
    
    def clean_graduation(self):
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
 
    # Global Variables
    INDUSTRIES = (
        ('', 'Select..'),
        ('Agriculture', 'Agriculture'),
        ('Banking', 'Banking'),
        ('Construction', 'Construction'),
        ('Chemical Development', 'Chemical Development'),
        ('Communications', 'Communications'),
        ('Computer Hardware', 'Computer Hardware'),
        ('Consumer Goods', 'Consumer Goods'),
        ('Energy Advancement', 'Energy Advancement'),
        ('Entertainment', 'Entertainment'),
        ('Food and Beverage', 'Food and Beverage'),
        ('Healthcare', 'Healthcare'),
        ('IT Services', 'IT Services'),
        ('Insurance', 'Insurance'),
        ('Media Relations', 'Media Relations'),
        ('Medical Facilites', 'Medical Facilities'),
        ('Political', 'Political'),
        ('Real Estate', 'Real Estate'),
        ('Services', 'Services'),
        ('Software Development', 'Software Development'),
        ('Transportation', 'Transportation'),
        ('Utilities', 'Utilities')
    )

    STATES = (
        ('', 'Select..'),
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'Dist of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
 

    name = forms.CharField(label=(u'Company Name'), max_length=30, required=True)
    ein = forms.CharField(label=(u'EIN'), min_length=9, max_length=9, required=True)
    description = forms.CharField(label=(u'Company Description'), widget=forms.Textarea, max_length=1250, required=False)
    industry = forms.ChoiceField(label=(u'Industry'), choices=INDUSTRIES, required=True)
    address = forms.CharField(label=(u'Company Address'), max_length=100, required=True)
    city = forms.CharField(label=(u'City'), max_length=22, required=True)
    state = forms.ChoiceField(label=(u'State'), choices=STATES, required=True)
    zip = forms.CharField(label=(u'Zip Code'), min_length=3, max_length=9, required=True)
    username = forms.CharField(label=(u'User Name'), required=True)
    email = forms.EmailField(label=(u'<abbr title="This is the email Intern Match will use to contact you. This email is never shared publicly.">Private Email Address</abbr>'), max_length=50, required=True)
    phone = forms.CharField(label=(u'<abbr title="This is the phone number that will be displayed to prospective interns. We recommend using a general point of contact.">Public Phone Number</abbr>'), max_length=15, required=True)
    contactEmail = forms.EmailField(label=(u'<abbr title="This is the email that will be displayed to prospective interns. We recommend using emails such as: careers@website.com">Public Email Address</abbr>'), max_length=50, required=True)
    website = forms.URLField(label=(u'Company Website'), max_length=100, required=False)
    password  = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False), required=True, min_length=6)
    password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False), required=True, min_length=6)
    agree_terms = forms.MultipleChoiceField(label = (u'In order to proceed, you must agree with our Terms of Service.'),required=True, 
                                                     choices = (('agree', "I have read, and agree to the Terms of Service."),), widget = forms.CheckboxSelectMultiple, 
                                                     help_text = "<a href='#termsModal' class='btn btn-mini' type='button' data-toggle='modal'>View Terms of Service</a>")
    
    class Meta:
        model = Profile
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
        return self.cleaned_data
