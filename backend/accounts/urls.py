from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterView, LoginView, MeView

urlpatterns = [
    #POST /api/auth/register/
    path("register/", RegisterView.as_view(), name="register"),
    #POST /api/auth/login/ 
    path("login/", LoginView.as_view(), name="login"),
    #POST /api/auth/refresh/
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    #GET /api/auth/profile/
    path("profile/", MeView.as_view(), name="profile"),
]
