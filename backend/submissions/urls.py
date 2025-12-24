# submissions/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubmissionViewSet


router = DefaultRouter()

# 2. تسجيل الـ ViewSet (هنا نحدد اسم المسار في المتصفح)
router.register(r'', SubmissionViewSet, basename='submission')
# المسارات التي سيتم توليدها تلقائياً:
# /submissions/ (GET, POST)
# /submissions/{pk}/ (GET, PUT, PATCH, DELETE)
# /submissions/{pk}/update-status/ (PATCH) <--- المسار المخصص
urlpatterns = [
    path('', include(router.urls)),
]