from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()

#SimpleJWT customization for sign in response
class LoginByJWT(TokenObtainPairSerializer):
    """
        Custom serializer to include:
         1. user data 
         2. (acccess & refresh token)
    """
    # check username and password and returns the data 
    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = UserSerializer(self.user).data
        return data

# loged in by SimpleJWT => tokens+user
class LoginView(TokenObtainPairView):
    serializer_class = LoginByJWT

#POST view for new user registration 
class CreateUserView(generics.CreateAPIView):
    """
        Public endpoint for user registration.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

#GET view for current user
class MeView(APIView):
    #only authenticated users can access this view
    permission_classes = [IsAuthenticated]
    #GET method implementation
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
