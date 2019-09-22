from django.db import models
from django.contrib.auth.models import AbstractUser


class WebUser(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
