from django.db import models
from register.models import Profile

class Resume(models.Model):
    date_posted = models.DateField()
    intern = models.ForeignKey(Profile)
    summary = models.TextField(max_length=250, null=True)
    
    def getReferences(self):
        return self.reference_set.all()
    
    def getSkills(self):
	return self.skill_set.all()

    def getActivities(self):
        return self.activy_set.all()
     
    def __unicode__(self):
        return self.intern

class Skill(models.Model):   
    name = models.CharField(max_length=50,null=True)
    resume = models.ForeignKey('Resume', null=True)    # skill could be part of resume
    intern = models.ForeignKey('register.Profile', null=True)      # skill could belong to intern
    
    def __unicode__(self):
        return self.name

class Experience(models.Model):
    intern = models.ForeignKey('register.Profile', null=True)      # Job/Project experience could belong to intern
    title = 
    company_class_name =
    start_date = 
    end_date = 
    city = 
    state = 
    description = 

    def __unicode__(self):
        return self.title

class Activity(models.Model):
    intern = models.ForeignKey('register.Profile', null=True)      # activity could belong to intern
    name = 

    def __unicode__(self):
        return self.name
    
class Reference(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    resume = models.ForeignKey('Resume', null=True)    # skill could be part of resume
    intern = models.ForeignKey('register.Profile', null=True)      # reference could belong to intern
    
    def __unicode__(self):
        return self.name    
