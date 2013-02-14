from django.db import models
from django.db.models.signals import post_save
from register.models import Profile
import random

# Create your models here.
class Quiz(models.Model):
    question = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question

class Option(models.Model):
    quiz = models.ForeignKey(Quiz)
    option_name = models.CharField(max_length=100)
    option_value = models.IntegerField()

    def __unicode__(self):
        return self.option_name
    
class QuizResult(models.Model):
    quiz = models.OneToOneField(Quiz)
    user = models.OneToOneField(Profile)
    quiz_string = models.CharField(max_length=100, null=True)
    quiz_result = models.IntegerField()

    @classmethod
    def create(cls, userID):
        q = cls(user_id=userID, quiz_string=None, quiz_result=None)
        q.save()
        return q

    # this def will handle the POST request data. For now, just filling with dummy data.
    def collectQuizData(self, quizString):
        self.quiz_string = quizString
        self.parseQuizString(quizString)
        self.save()

    # using this def, the professor can call his script to take:
    #      self.quiz_result = os.system('gfortran qsrtScript.f -d %s' % self.quiz_string)
    # or something like that
    def parseQuizString(self, quizData):
        self.quiz_result = random.randrange(1,6)

    def findUserScore(self, userID):
        return Quiz.objects.filter(user_id = userID)

    # could prove useful when creating the Company Profile page to list all Intern objects that match.
    def findSimiliarUsers(self, quizResult):
        return Quiz.objects.filter(quiz_result = quizResult)

    def __unicode__(self):
        return self.quiz_string
