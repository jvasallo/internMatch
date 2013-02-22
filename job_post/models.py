from django.db import models
from register.models import Profile

class JobPost(models.Model):
    date_posted    = models.DateField(null=True)
    date_post_ends = models.DateField(null=True)
    company        = models.ForeignKey(Profile)
    description    = models.CharField(max_length=250, null=True)
    headline       = models.CharField(max_length=50, null=True)
    
    def __unicode__(self):
        return self.headline
    
    
class Skill(models.Model):
    name              = models.CharField(max_length=25,null=True)
    job_post          = models.ForeignKey('JobPost')
    intern_or_company = models.ForeignKey('register.Profile')
    
    def __unicode__(self):
        return self.name
    