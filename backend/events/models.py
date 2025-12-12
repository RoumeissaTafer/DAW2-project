from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError

User = settings.AUTH_USER_MODEL


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    theme = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField()
    start_date = models.DateField()
    end_date = models.DateField()
    # status, submission deadlines, registiration deadlines, check(end_date > start_date)

    # one organizer only
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="managed_events",
    )
    reviewers = models.ManyToManyField(
        User,
        related_name="reviewer_in_events",
        blank=True,
    )
    guests = models.ManyToManyField(
        User,
        related_name="guest_in_events",
        blank=True,
    )

    registration_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return self.title

    @property
    def is_archived(self):
        return self.end_date < timezone.now().date()


class Session(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="sessions",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    room = models.CharField(max_length=255, blank=True)
    speaker = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sessions_as_speaker",
    )

    def __str__(self):
        return f"{self.title} ({self.event.title})"

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

    # Animator of the workshop
    animator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="animated_workshops",
    )

    # The animator who can set nb of slots and manage registrations
    max_slots = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date", "start_time"]

    def __str__(self):
        return f"{self.title} ({self.event.title})"

    @property
    def confirmed_count(self):
        return self.registrations.filter(status=WorkshopRegistration.Status.CONFIRMED).count()

    @property
    def remaining_slots(self):
        return max(self.max_slots - self.confirmed_count, 0)


class WorkshopRegistration(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        CONFIRMED = "CONFIRMED", "Confirmed"
        CANCELLED = "CANCELLED", "Cancelled"

    workshop = models.ForeignKey(
        Workshop,
        on_delete=models.CASCADE,
        related_name="registrations",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="workshop_registrations",
    )

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.CONFIRMED)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("workshop", "user")

    def __str__(self):
        return f"{self.user} -> {self.workshop} ({self.status})"

    def clean(self):
        """
         important validations before saving a workshop registration
                1. the user must be registered in the event of the workshop
        """
        # the user must be registered in the event of the workshop
        if not Registration.objects.filter(event=self.workshop.event, user=self.user).exists():
            raise ValidationError("You must first be registered in the event of the workshop.")

        # confirmed registrations count
        confirmed = WorkshopRegistration.objects.filter(
            workshop=self.workshop,
            status=WorkshopRegistration.Status.CONFIRMED
        ).exclude(pk=self.pk).count()

        if self.status == WorkshopRegistration.Status.CONFIRMED and confirmed >= self.workshop.max_slots:
            raise ValidationError("The workshop has reached its maximum number of confirmed registrations.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
