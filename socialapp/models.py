from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Tags(models.Model):
    name = models.CharField(max_length=250)



class Story(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250)
    weight = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    # upload = models.ImageField(upload_to="media/story-images", null=True, blank=True)


class Image(models.Model):
    story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    upload = models.ImageField(upload_to="media/story-images", null=True, blank=True)

class StoryStatus(models.Model):
    STORY_STATUS = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )
    story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STORY_STATUS)

# class Weightage(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
#     weight = models.IntegerField(default=0)
#
#     def get_full_name(self):
#         return self.user.first_name
