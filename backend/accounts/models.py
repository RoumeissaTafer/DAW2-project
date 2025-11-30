from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    #fields must add them
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    
    #user role
    ROLE_CHOICES = [
        ('ORGANIZER', 'Organizer'),
        ('COMMUNICANT', 'Communicant'),
        ('REVIEWER', 'Reviewer'),
        ('PARTICIPANT', 'Participant'),
        ('GUEST', 'Guest'),
        ('ANIMATOR', 'Workshop Animator'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    #extra fields
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    organization = models.CharField(max_length=255, null=True, blank=True)

    # User logs in with email, not username
    USERNAME_FIELD = 'email'
    #requires it when creating accounts
    REQUIRED_FIELDS = ['username']
