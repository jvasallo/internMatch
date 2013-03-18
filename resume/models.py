from django.db import models
from register.models import Profile

class Reference(models.Model):
    profile = models.ForeignKey(Profile, unique=False, null=False)      # reference could belong to intern
    name = models.CharField(max_length=50,null=True)
    relationship = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50,null=True)
    
    def __unicode__(self):
        return self.name    
