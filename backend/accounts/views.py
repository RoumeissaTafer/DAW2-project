from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

#SimpleJWT customization for login response
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    # check username and password and returns the data 
    def validate(self, attrs):
        # Call the superclass method to validate the credentials
        data = super().validate(attrs)
        # Add new data response and store it in data variable
        data["user"] = UserSerializer(self.user).data
        return data

# loged in by SimpleJWT => tokens+user
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

#POST view for new user registration
class RegisterView(generics.CreateAPIView):
    #to tell view which model to work with
    queryset = User.objects.all()
    #data comes from frontend to backend
    serializer_class = RegisterSerializer
    #anyone can access this view
    permission_classes = [permissions.AllowAny]

#GET view for current user
class MeView(APIView):
    #only authenticated users can access this view
    permission_classes = [permissions.IsAuthenticated]
    #GET method implementation
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
