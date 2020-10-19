from django.db import models

# Create your models here.
class Hobby(models.Model):
    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)
    #hobby_picture=models
