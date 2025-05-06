from django.contrib import admin

# Register your models here.
# admin.py
from .models import UserProfile

admin.site.register(UserProfile)
