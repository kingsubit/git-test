from django.contrib import admin
from .models import CustomUser  # 이 줄이 오류 없이 작동해야 함

admin.site.register(CustomUser)
