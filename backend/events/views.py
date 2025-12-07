from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from .models import Event, Session
from .serializers import EventSerializer, SessionSerializer
from .permissions import IsOrganizerOrAdminOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("start_date")
    serializer_class = EventSerializer
    permission_classes = [IsOrganizerOrAdminOrReadOnly]

    def perform_create(self, serializer):
        # creator of the event becomes its admin
        serializer.save(admin=self.request.user)

    @action(detail=False, methods=["get"])
    def upcoming(self, request):
        """
        GET /api/events/upcoming/
        Returns events with end_date >= today
        """
        today = timezone.now().date()
        qs = Event.objects.filter(end_date__gte=today).order_by("start_date")
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def archived(self, request):
        """
        GET /api/events/archived/
        Returns events with end_date < today
        """
        today = timezone.now().date()
        qs = Event.objects.filter(end_date__lt=today).order_by("-start_date")
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by("start_datetime")
    serializer_class = SessionSerializer
    # you can later restrict this (e.g., only organizers / animators)
    # for now: any authenticated user could create sessions, or restrict:
    # permission_classes = [IsOrganizerOrAdminOrReadOnly]
