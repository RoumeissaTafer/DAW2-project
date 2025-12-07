from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Event(models.Model):
    """
    Scientific event (colloque, journée scientifique, workshop day, etc.)
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    theme = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField()

    start_date = models.DateField()
    end_date = models.DateField()

    # the organizer who created this event (backend admin of this event)
    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="managed_events",
    )

    # scientific committee members (users with role REVIEWER usually)
    scientific_committee = models.ManyToManyField(
        User,
        related_name="committee_events",
        blank=True,
    )

    # invited speakers / guests
    invited_speakers = models.ManyToManyField(
        User,
        related_name="speaker_events",
        blank=True,
    )

    # optional: link to registration form on frontend
    registration_link = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return self.title

    @property
    def is_archived(self):
        from django.utils import timezone

        return self.end_date < timezone.now().date()


class Session(models.Model):
    """
    One session / slot inside an event program:
    keynote, panel, workshop, etc.
    """

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="sessions",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # when this session happens
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    room = models.CharField(max_length=255, blank=True)

    # optional: link to a user as speaker
    speaker = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sessions_as_speaker",
    )

    def __str__(self):
        return f"{self.title} ({self.event.title})"
