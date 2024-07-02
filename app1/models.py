from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    USER_CHOICES = [
        (1, "hd"),
        (2, "staff"),
        (3, "student")
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_CHOICES, default=1)
    pr_pic = models.ImageField(upload_to='profile_pics/')

 