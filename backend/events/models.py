from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver

User = settings.AUTH_USER_MODEL

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    theme = models.CharField(max_length=255, blank=True)
    
    start_date = models.DateField()
    end_date = models.DateField()

    contact_email = models.EmailField()

    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="managed_event",
    )
    
    class Meta:
        ordering = ["start_date"]
    
    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("end_date must be >= start_date")

    @property
    def is_archived(self):
        return self.end_date < timezone.now().date()

    def __str__(self):
        return self.title

class EventMember(models.Model):

    event = models.ForeignKey(
        Event, 
        on_delete=models.CASCADE, 
        related_name="members"
    )
    email = models.EmailField()
    role = models.CharField(max_length=30)

    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("event", "email", "role")
    
    def clean(self):
        if self.role not in ("REVIEWER", "GUEST"):
            raise ValidationError("role must be REVIEWER or GUEST")

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def link_event_members_to_user(sender, instance, created, **kwargs):
    if getattr(instance, "email", None):
        EventMember.objects.filter(user__isnull=True, email__iexact=instance.email).update(user=instance)

class Workshop(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="workshops",
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=255, blank=True)
    max_slots = models.PositiveIntegerField(default=30)

    animator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="animated_workshops",
    )

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError("end_time must be > start_time")

    class Meta:
        ordering = ["date", "start_time"]

    def __str__(self):
        return f"{self.title} ({self.event.title})"
