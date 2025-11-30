from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


# --- USER MANAGER ---
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


# --- USER MODEL ---
class User(AbstractBaseUser, PermissionsMixin):

    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    ROLE_CHOICES = [
        ('ORGANIZER', 'Organizer'),
        ('COMMUNICANT', 'Communicant'),
        ('REVIEWER', 'Reviewer'),
        ('PARTICIPANT', 'Participant'),
        ('GUEST', 'Guest'),
        ('ANIMATOR', 'Animator'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    #extra fields
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    organization = models.CharField(max_length=255, null=True, blank=True)

    # Required for Django auth
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Login with email
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # Connect manager
    objects = UserManager()

    def __str__(self):
        return self.email
