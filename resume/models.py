from django.db import models
from register.models import Profile

class Experience(models.Model):
    intern = models.ForeignKey('register.Profile', null=True)      # Job/Project experience could belong to intern
    title = models.CharField(max_length=50,null=True)
    company_class_name = models.CharField(max_length=50,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    city = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=50,null=True)

    def __unicode__(self):
        return self.title

class Reference(models.Model):
    profile = models.ForeignKey(Profile, unique=False, null=False)      # reference could belong to intern
    name = models.CharField(max_length=50,null=True)
    relationship = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50,null=True)
    
    def __unicode__(self):
        return self.name    
