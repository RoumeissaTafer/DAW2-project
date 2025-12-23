from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CreateUserView, LoginView, MeView

urlpatterns = [
    #POST /api/auth/register/
    path("register/", CreateUserView.as_view(), name="register"),
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'),
    #POST /api/auth/refresh/
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    #GET /api/auth/profile/
    path("profile/", MeView.as_view(), name="profile"),
   #POST /api/auth/login/ 
    path("login/", LoginView.as_view(), name="login"),
]
    
