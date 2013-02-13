from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import random

class Profile(models.Model):
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


class Quiz(models.Model):
    user_id = models.IntegerField()
    quiz_string = models.CharField(max_length=100, null=True)
    quiz_result = models.IntegerField()

    @classmethod
    def create(cls, userID):
        q = cls(user_id=userID, quiz_string=None, quiz_result=0) 
                   # Link this to David's user Model, update this via post, update via def
        q.save()
        return q

    # this def will handle the POST request. For now, just filling with dummy data.
    def collectQuizData(self, request):
        self.quiz_string = request  # change this to the POST request
        self.parseQuizString(request)
        self.save()

    # using this def, the professor can call his script to take:
    #      self.quiz_result = os.system('gfortran qsrtScript.f -d %s' % self.quiz_string)
    # or something like that
    def parseQuizString(self, quizData):
        self.quiz_result = random.randrange(1, 6)
        
    def findUserScore(self, userID):
        return Quiz.objects.filter(user_id=userID)    

    # could prove useful when creating the Company Profile page to list all Intern objects that match.
    def findSimiliarUsers(self, quizResult):
        return Quiz.objects.filter(quiz_result=quizResult)    

    def __unicode__(self):
        return self.quiz_string
