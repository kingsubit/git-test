from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    student_number = models.CharField(max_length=20, null=True, blank=True, default="기본값")

    USERNAME_FIELD = 'email'  # 로그인에 사용할 필드
    REQUIRED_FIELDS = ['username']  # createsuperuser 시 필요한 필드

    def __str__(self):
        return self.email

from django.db import models
from .models import CustomUser

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username




