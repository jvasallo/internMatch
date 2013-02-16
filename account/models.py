from django.db import models
from django.contrib.auth.models import User

# This is just the start we can add or take away fields from here as needed
# This is from an old template I had.

class InternProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    url = models.URLField("Website", blank=True)
    company = models.CharField(max_length=50, blank=True)

class CompanyProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    url = models.URLField("Website", blank=True)
    company = models.CharField(max_length=50, blank=True)
