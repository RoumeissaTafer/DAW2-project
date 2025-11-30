from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ROLE_CHOICES = [
        ('SUPER_ADMIN', 'Super Admin'),
        ('ADMIN', 'Organizer'),
        ('COMMUNICANT', 'Communicant'),
        ('COMMITTEE_MEMBER', 'Reviewer'),
        ('PARTICIPANT', 'Participant'),
        ('SPEAKER', 'Invited Speaker'),
        ('WORKSHOP_ANIMATOR', 'Workshop Animator'),
    ]

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='PARTICIPANT')

    # Extra optional fields
    bio = models.TextField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)

    # Profile picture field
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
