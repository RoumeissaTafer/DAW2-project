from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Event, Session

User = get_user_model()


class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "role"]


class SessionSerializer(serializers.ModelSerializer):
    speaker = UserMiniSerializer(read_only=True)

    class Meta:
        model = Session
        fields = [
            "id",
            "title",
            "description",
            "start_datetime",
            "end_datetime",
            "room",
            "speaker",
        ]


class EventSerializer(serializers.ModelSerializer):
    admin = UserMiniSerializer(read_only=True)
    scientific_committee = UserMiniSerializer(many=True, read_only=True)
    invited_speakers = UserMiniSerializer(many=True, read_only=True)
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "location",
            "theme",
            "contact_email",
            "start_date",
            "end_date",
            "registration_link",
            "admin",
            "scientific_committee",
            "invited_speakers",
            "sessions",
            "is_archived",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["admin", "created_at", "updated_at", "is_archived"]
