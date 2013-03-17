from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist


class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30, null=True)
    ein = models.CharField(max_length=9, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=22, null=True)
    state = models.CharField(max_length=20, null=True)
    zip = models.CharField(max_length=10, null=True)
    school = models.CharField(max_length=80, null=True)
    phone = models.CharField(max_length=15, null=True)
    contactEmail = models.CharField(max_length=50, null=True)
    website = models.CharField(max_length=100, null=True)
    graduation_date = models.DateField(null=True)
    major = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=20, null=True)
    industry = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=1250, null=True)
    is_intern = models.BooleanField()

    def formattedDate(self):
        return self.graduation_date.strftime("%Y-%m-%d")

    def quizResult(self):
        try:
            q = self.user.quizresult_set.get()
        except ObjectDoesNotExist:
            return None
        result = q.quiz_result
        return result

    def getActiveJobs(self):
        activeJobs = []
        for job in self.jobpost_set.all():
            if job.active():
                activeJobs.append(job)
        return activeJobs

    def getReferences(self):
        return self.reference_set.all()

    def getSkills(self):
        return self.skill_set.all()

    def getSkillList(self):
        skillList = []
        for eachSkill in self.skill_set.all():
            skillList.append(eachSkill.name)
        skills = ",".join(skillList)
        return skills

    def __unicode__(self):
        return unicode(self.name)


def create_profile_callback(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#    else:
#        Profile.objects.update(user=instance)


post_save.connect(create_profile_callback, sender=User)


