from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.CharField(max_length = 30)
    about = models.CharField(max_length = 300)
    profile_picture = models.CharField(max_length = 500)
