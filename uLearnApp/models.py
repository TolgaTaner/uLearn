from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class sub_category(models.Model):
    name = models.CharField(max_length = 100)
class category(models.Model):
    name = models.CharField(max_length = 100)
    sub_category = models.ForeignKey(sub_category, on_delete = models.CASCADE, default = None)
class lesson(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 300)
    owner = models.OneToOneField(User, on_delete = models.CASCADE)
    thumbnail = models.CharField(max_length = 1000)
    preview_video_path  = models.CharField(max_length = 1000)
    category = models.OneToOneField(category, on_delete=models.CASCADE)
    sub_category = models.OneToOneField(sub_category, on_delete = models.CASCADE)
    created_date = models.DateField(default = datetime.now())
class lectures(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    duration = models.IntegerField(default = 0)
    video_url = models.CharField(max_length = 1000)
    lesson = models.ForeignKey(lesson, on_delete = models.CASCADE, default = None)
class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.CharField(max_length = 30)
    about = models.CharField(max_length = 300)
    profile_picture = models.CharField(max_length = 500)
    lesson = models.ManyToManyField(lesson)
