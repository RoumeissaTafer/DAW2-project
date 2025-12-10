"""
    Convert Python objects → JSON
    Convert JSON → Python objects
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model

# Get the custom user model
User = get_user_model()

# To get user data and serialize it to JSON 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "role", "username", "email", "first_name", "last_name", "institution", "bio", "photo"]
        """ 
            user can't change his id and username 
        """
        read_only_fields = ["id", "username"]

# To handle new users registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name", "role"]

    def validated_role(self, value):
        allowed_roles = [
            User.Roles.ORGANIZER,
            User.Roles.AUTHOR,
            User.Roles.PARTICIPANT,
            User.Roles.ANIMATOR,
        ]
        if value not in allowed_roles:
            raise serializers.ValidationError(" Vous ne pouvez pas choisir ce rôle.")
        return value
    
    def create(self, validated_data):
        # Create a new user with encrypted password
        password = validated_data.pop("password")
        # Use the custom user model's create_user method to handle password hashing
        user = User.objects.create_user(password=password, **validated_data)
        return user

