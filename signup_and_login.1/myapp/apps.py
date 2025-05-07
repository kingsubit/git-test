from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        # Django 앱이 완전히 로드된 후에 임포트가 이루어집니다
        from django.contrib.auth.models import AbstractUser


