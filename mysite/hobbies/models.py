from django.db import models

# Create your models here.
class Hobby(models.Model):
    def __str__(self):
        return self.hobby_name

    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)
    hobby_picture=models.CharField(max_length=500, default="https://icebreakerideas.com/wp-content/uploads/2018/07/57-Best-List-of-Hobbies-For-Men-and-Women.jpeg")
