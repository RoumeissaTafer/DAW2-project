from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=30, default="PARTICIPANT")
    institution = models.CharField(max_length=255, blank=True)
    domain = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="profiles/", null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
