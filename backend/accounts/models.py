from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", "Super Administrateur"
        ORGANIZER = "ORGANIZER", "Organisateur"
        COMMITTEE = "COMMITTEE", "Membre du comité"
        AUTHOR = "AUTHOR", "Communicant / Auteur"
        PARTICIPANT = "PARTICIPANT", "Participant"
        INVITED = "INVITED", "Invité / Conférencier"
        WORKSHOP_ANIMATOR = "WORKSHOP_ANIMATOR", "Animateur de workshop"

    role = models.CharField(
        max_length=30,
        choices=Roles.choices,
        default=Roles.PARTICIPANT,
    )
    institution = models.CharField(max_length=255, blank=True)
    domain = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="profiles/", blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
