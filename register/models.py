from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    zip = models.CharField(max_length=10, null=True)
    school = models.CharField(max_length=80, null=True)
    phone = models.CharField(max_length=15, null=True)
    contactEmail = models.CharField(max_length=50, null=True)
    website = models.CharField(max_length=100, null=True)
    graduation_date = models.DateField(null=True)
    major = models.CharField(max_length=50, null=True)
    industry = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=1250, null=True)
    is_intern = models.BooleanField()

    def formattedDate(self):
        return self.graduation_date.strftime("%Y-%m-%d")
    
    def quizResult(self):
        q = self.user.quizresult_set.get()
        result = q.quiz_result
        return result

    def skills(self):
        return self.skill_set.filter(profile=self)

    def __unicode__(self):
        return self.name
    
    
    def create_profile_callback(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
   #    else:
   #        Profile.objects.update(user=instance)


    post_save.connect(create_profile_callback, sender=User)


