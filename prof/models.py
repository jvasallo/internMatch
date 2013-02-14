from django.db import models

# Create your models here.
class Prof(models.Model):
    name = models.CharField(max_length=50)
    
class Skills(models.Model):
    skill = models.CharField(max_length=30)
    summary = models.CharField(max_length = 200)