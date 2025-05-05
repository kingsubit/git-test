from django.db import models

# Create your models here.

class User(models.Model):
    username = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.username
