from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Intern(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)
    school = models.CharField(max_length=80)
    graduation_date = models.DateField()
    major = models.CharField(max_length=50)
    
    
    def __unicode__(self):
        return self.name
    
#def create_intern_user_callback(sender, instance, **kwargs):
#    intern , new = User.objects.get_or_create(user=instance)
#post_save.connect(create_intern_user_callback, User)