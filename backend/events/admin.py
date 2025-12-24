<<<<<<< HEAD
from django.contrib import admin
from .models import Event, EventMember, Workshop


class EventMemberInline(admin.TabularInline):
    model = EventMember
    extra = 0


class WorkshopInline(admin.TabularInline):
    model = Workshop
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "start_date", "end_date", "organizer")
    list_filter = ("start_date", "end_date", "location")
    search_fields = ("title", "theme", "location", "organizer__username", "organizer__email")
    inlines = [EventMemberInline, WorkshopInline]


@admin.register(EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    list_display = ("event", "email", "role", "user", "created_at")
    list_filter = ("role", "created_at")
    search_fields = ("email", "event__title", "user__username", "user__email")


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ("title", "event", "animator", "start_datetime", "end_datetime")
    list_filter = ("start_datetime", "event")
    search_fields = ("title", "event__title", "animator__username", "animator__email")
=======
from django.contrib import admin
#lazem tzidi hadou beh ykhrjou fi admin page normalement
from .models import Event, Session
admin.site.register(Event)
admin.site.register(Session)
>>>>>>> hiba
