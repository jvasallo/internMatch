from django.db import models
from register.models import Profile

class JobPost(models.Model):
    date_posted    = models.DateField()
    date_post_ends = models.DateField()
    company        = models.ForeignKey(Profile)
    description    = models.TextField(max_length=250, null=True)
    company_bio    = models.TextField(max_length=250, null=True)
    position       = models.CharField(max_length=50)
    headline       = models.CharField(max_length=50, null=True)
    city           = models.CharField(max_length=50, null=True)
    state          = models.CharField(max_length=50, null=True)

    def formattedDate(self):
        return self.date_post_ends.strftime("%Y-%m-%d")
    
    def getRequiredSkills(self):
        return self.skill_set.filter(type='required')
    
    def getDesiredSkills(self):
        return self.skill_set.filter(type='desired')

    def __unicode__(self):
        return self.headline
    
    
class Skill(models.Model):
    name              = models.CharField(max_length=50,null=True)
    type              = models.CharField(max_length=15,null=False) # desired or required skill
    job_post          = models.ForeignKey('JobPost', null=True)    # skill could be part of job_post 
    intern            = models.ForeignKey('register.Profile', null=True)      # skill could belong to intern
    
    def __unicode__(self):
        return self.name
    
