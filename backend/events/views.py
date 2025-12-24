from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Event, EventMember, Workshop
from .serializers import EventSerializer, EventMemberSerializer, WorkshopSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if getattr(self.request.user, "role", None) != "ORGANIZER":
            raise PermissionDenied("Only ORGANIZER can create events.")
        serializer.save(organizer=self.request.user)

    def perform_update(self, serializer):
        event = self.get_object()
        if event.organizer != self.request.user:
            raise PermissionDenied("Only the organizer can update this event.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.organizer != self.request.user:
            raise PermissionDenied("Only the organizer can delete this event.")
        instance.delete()


class EventMemberViewSet(viewsets.ModelViewSet):
    serializer_class = EventMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return EventMember.objects.filter(event__organizer=self.request.user).select_related("event", "user")

    def perform_create(self, serializer):
        event = serializer.validated_data["event"]
        if event.organizer != self.request.user:
            raise PermissionDenied("Only the organizer can add members.")
        serializer.save()


class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all().select_related("event", "animator")
    serializer_class = WorkshopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if getattr(self.request.user, "role", None) != "ANIMATOR":
            raise PermissionDenied("Only ANIMATOR can create workshops.")
        serializer.save(animator=self.request.user)
