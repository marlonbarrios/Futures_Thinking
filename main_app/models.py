from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from taggit.managers import TaggableManager



class UserEntries(models.Model):
     future = models.CharField(max_length=350)
     title = models.CharField(max_length=100)
     tags = TaggableManager()
     optional_image = models.CharField(max_length=250, blank=True)
     optional_video = EmbedVideoField(blank=True)
     date = models.DateTimeField(auto_now=True)
     user = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
        return self.title
        # return f"{self.title} was created on {self.date} with the id of {self.id}"

     def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.id})
    

class AllEntries(models.Model):
    user_entries = models.ForeignKey(UserEntries, on_delete=models.CASCADE)

    def __str__(self):
        return f"This user entry is from {self.user_entries}"

# set email for login
USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['username']

