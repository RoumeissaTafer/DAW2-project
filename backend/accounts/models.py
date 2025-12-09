from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
        extended Django’s authentication system 
        by creating our own model
    """
    class Roles(models.TextChoices):
        OWNER = "Super Administrateur "
        ORGANIZER = "Organisateur d’événement"
        AUTHOR = "Communicant / Auteur"
        REVIEWER = "Membre du Comité  scientifique"
        PARTICIPANT = "Participant"
        GUEST = "Invité / Conférencier"
        ANIMATOR = "Animateur de Workshop "

    role = models.CharField(
        max_length=30,
        choices=Roles.choices,
        default=Roles.PARTICIPANT,
    )
    institution = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="profiles/", blank=True, null=True)

    #Return name (role) of the user on admin page.
    def __str__(self):
        return f"{self.username} ({self.role})"


