from django.db import models
from django.contrib.auth.models import User
from register.models import Profile

# This is just the start we can add or take away fields from here as needed
# This is from an old template I had.

class InternProfile(models.Model):
    user = models.ForeignKey(User, unique=True)	
    profile = models.ForeignKey(Profile)
    url = models.URLField("Website", blank=True)
    summary = models.CharField(max_length=300, blank=True)
    skills = models.CharField(max_length=20, blank=True)
    experience = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=50, blank=True)
    GRADE_LEVEL = (
        (u'FR', u'Freshman'),
        (u'SO', u'Sophomore'),
        (u'JR', u'Junior'),
        (u'SR', u'Senior'),
        (u'GR', u'Graduate'),
    )
    grade = models.CharField(max_length=2, choices=GRADE_LEVEL)
    
class CompanyProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    url = models.URLField("Website", blank=True)
    company = models.CharField(max_length=50, blank=True)
