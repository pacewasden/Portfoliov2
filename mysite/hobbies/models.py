from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Hobby(models.Model):
    def __str__(self):
        return self.hobby_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)
    hobby_picture = models.CharField(max_length=500, default="https://icebreakerideas.com/wp-content/uploads/2018/07/57-Best-List-of-Hobbies-For-Men-and-Women.jpeg")

    def get_absolute_url(self):
        return reverse("hobbies:detail", kwargs={"pk": self.pk})
