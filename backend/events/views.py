from rest_framework import viewsets, permissions
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    # user must be logged in to access these views
    permission_classes = [permissions.IsAuthenticated]  

    def get_queryset(self):
        # Return only events created by current user
        return Event.objects.filter(admin=self.request.user)

    def perform_create(self, serializer):
        # Automatically set admin = current user
        serializer.save(admin=self.request.user)
