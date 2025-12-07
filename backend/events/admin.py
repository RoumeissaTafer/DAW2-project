from django.contrib import admin
from .models import Event, Session


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date", "location", "admin")
    list_filter = ("start_date", "location", "theme")
    search_fields = ("title", "location", "theme")
    filter_horizontal = ("scientific_committee", "invited_speakers")


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("title", "event", "start_datetime", "end_datetime", "room", "speaker")
    list_filter = ("event",)
    search_fields = ("title", "event__title", "room")
