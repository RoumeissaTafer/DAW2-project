from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
        extended Django authentication system 
        by creating our own model
    """
    class Roles(models.TextChoices):
        ORGANIZER = "ORGANIZER", "Organisateur d’événement"
        AUTHOR = "AUTHOR", "Communicant / Auteur"
        REVIEWER = "REVIEWER", "Membre du Comité scientifique"
        PARTICIPANT = "PARTICIPANT", "Participant"
        GUEST = "GUEST", "Invité / Conférencier"
        ANIMATOR = "ANIMATOR", "Animateur de Workshop"

    role = models.CharField(max_length=30, choices=Roles.choices, default=Roles.PARTICIPANT)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="profiles/", blank=True, null=True)

    #Return name (role) of the user on admin page.
    def __str__(self):
        return f"{self.username} ({self.role})" 
