from rest_framework.routers import DefaultRouter
from .views import EventViewSet, SessionViewSet

router = DefaultRouter()
router.register(r"events", EventViewSet, basename="event")
router.register(r"sessions", SessionViewSet, basename="session")

urlpatterns = router.urls
