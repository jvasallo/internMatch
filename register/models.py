from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Intern(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=20, null=True)
    zip = models.CharField(max_length=10, null=True)
    school = models.CharField(max_length=80, null=True)
    graduation_date = models.DateField(null=True)
    major = models.CharField(max_length=50, null=True)
    
    
    def __unicode__(self):
        return self.name
    
def create_intern_user_callback(sender, instance, created, **kwargs):
    if created:
        import pdb; pdb.set_trace()
        Intern.objects.create(user=instance)
        
post_save.connect(create_intern_user_callback, sender=User)