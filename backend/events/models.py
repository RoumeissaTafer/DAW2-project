from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title
