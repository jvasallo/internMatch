from django.db import models
from register.models import Profile

class JobPost(models.Model):
    date_posted    = models.DateField(null=True)
    date_post_ends = models.DateField(null=True)
    company        = models.ForeignKey(Profile)
    description    = models.TextField(max_length=250, null=True)
    company_bio    = models.TextField(max_length=250, null=True)
    headline       = models.CharField(max_length=50, null=True)
    city           = models.CharField(max_length=50, null=True)
    state          = models.CharField(max_length=50, null=True)
    
    def __unicode__(self):
        return self.headline
    
    
class Skill(models.Model):
    name              = models.CharField(max_length=50,null=True)
    type              = models.CharField(max_length=15,null=False) # desired or required skill
    job_post          = models.ForeignKey('JobPost', null=True)    # skill could be part of job_post 
    intern            = models.ForeignKey('register.Profile', null=True)      # skill could belong to intern
    
    def __unicode__(self):
        return self.name
    