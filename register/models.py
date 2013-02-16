from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=20, null=True)
    zip = models.CharField(max_length=10, null=True)
    school = models.CharField(max_length=80, null=True)
    graduation_date = models.DateField(null=True)
    major = models.CharField(max_length=50, null=True)
    is_intern = models.BooleanField()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        permissions = (
                       ("intern", "Is the user an intern"),
                       )
    
def create_profile_callback(sender, instance, created, **kwargs):
    if created:
#        import pdb; pdb.set_trace()
        Profile.objects.create(user=instance)
#    else:
#        Profile.objects.update(user=instance)


post_save.connect(create_profile_callback, sender=User)
