from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
        extended Django’s authentication system 
        by creating our own model
    """
    class Roles(models.TextChoices):
        ORGANIZER = "ORGANIZER"
        AUTHOR = "AUTHOR"
        REVIEWER = "COMMITTEE"
        PARTICIPANT = "PARTICIPANT"
        GUEST = "INVITED"
        ANIMATOR = "WORKSHOP_ANIMATOR"

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


""" في ملف accounts/models.py قمت بإنشاء موديل مستخدم مخصص User يرث من AbstractUser.
أضفت حقل role بداخلها باستخدام TextChoices لتعريف الأدوار المختلفة.
كذلك أضفت حقول إضافية مثل institution, bio, و photo حتى نتمكن من تخزين معلومات أكثر عن المستخدمين.
هذا يسمح لنا لاحقًا بتطبيق صلاحيات مختلفة حسب الدور، مثل أن إنشاء الأحداث يكون مقتصرًا على المنظمين فقط."""