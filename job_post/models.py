from django.db import models
from register.models import Profile
import datetime

class JobPost(models.Model):
    date_posted    = models.DateField()
    date_post_ends = models.DateField()
    company        = models.ForeignKey(Profile)
    description    = models.TextField(max_length=250, null=True)
    company_bio    = models.TextField(max_length=250, null=True)
    position       = models.CharField(max_length=50)
    headline       = models.CharField(max_length=50, null=True)
    city           = models.CharField(max_length=50)
    state          = models.CharField(max_length=50)
    url            = models.URLField(max_length=200, null=True)

    def active(self):
        if self.date_post_ends > datetime.date.today():
            return True
        else:
            return False

    def fixUrl(self):
  	if "http://" not in self.url:
            return "http://%s" % self.url
        else:
            return self.url

    def formattedDate(self):
        return self.date_post_ends.strftime("%Y-%m-%d")
    
    def getRequiredSkills(self):
        return self.skill_set.filter(type='required')

    def getReqSkillList(self):
        skillList = []
        for eachSkill in self.skill_set.filter(type='required'):
            skillList.append(eachSkill.name)
        skills = ",".join(skillList)
        return skills

    def getDesiredSkills(self):
        return self.skill_set.filter(type='desired')

    def getDesSkillList(self):
        skillList = []
        for eachSkill in self.skill_set.filter(type='desired'):
            skillList.append(eachSkill.name)
        skills = ",".join(skillList)
        return skills

    def __unicode__(self):
        return self.headline
    
    
class Skill(models.Model):
    name              = models.CharField(max_length=50,null=True)
    type              = models.CharField(max_length=15,null=True) # desired or required skill
    job_post          = models.ForeignKey('JobPost', null=True)    # skill could be part of job_post 
    profile           = models.ForeignKey(Profile, null=True)      # skill could belong to intern
    
    def __unicode__(self):
        return self.name
    
