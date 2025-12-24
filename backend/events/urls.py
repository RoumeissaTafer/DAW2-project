<<<<<<< HEAD
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import EventViewSet, EventMemberViewSet, WorkshopViewSet

router = DefaultRouter()
router.register(r"events", EventViewSet, basename="events")
router.register(r"event-members", EventMemberViewSet, basename="event-members")
router.register(r"workshops", WorkshopViewSet, basename="workshops")

urlpatterns = [
    path("", include(router.urls)),
]
=======
from rest_framework.routers import DefaultRouter

urlpatterns = [
 
]
>>>>>>> hiba
