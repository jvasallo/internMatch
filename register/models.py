from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Intern(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
def create_intern_user_callback(sender, instance, **kwargs):
    intern , new = User.objects.get_or_create(user=instance)
post_save.connect(create_intern_user_callback, User)