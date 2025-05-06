from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)  # 이메일을 고유한 필드로 설정
    # 다른 필요한 필드 추가 가능

    USERNAME_FIELD = 'email'  # 이메일을 기본 로그인 필드로 설정
    REQUIRED_FIELDS = ['username']  # 이 필드는 관리자 생성 시 필수 필드

from django.db import models
from .models import CustomUser

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username



