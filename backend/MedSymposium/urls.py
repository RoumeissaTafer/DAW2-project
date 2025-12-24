from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include("accounts.urls")),
<<<<<<< HEAD
    path("api/event/", include("events.urls")),
=======
    path("api/events/", include("events.urls")),
    path("api/submissions/", include("submissions.urls")),    
>>>>>>> hiba
]
from django.conf.urls.static import static
from django.conf import settings
# To open the file path pdf
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)