from rest_framework import serializers
from .models import Event, EventMember, Workshop


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.StringRelatedField(read_only=True)
    is_archived = serializers.BooleanField(read_only=True)

    class Meta:
        model = Event
        fields = [
            "id","title","description","location","theme",
            "start_date","end_date",
            "contact_email","registration_link",
            "organizer","is_archived",
        ]
        read_only_fields = ["id","organizer","is_archived"]

    def validate(self, attrs):
        start = attrs.get("start_date", getattr(self.instance, "start_date", None))
        end = attrs.get("end_date", getattr(self.instance, "end_date", None))
        if start and end and end < start:
            raise serializers.ValidationError("end_date must be >= start_date")
        return attrs


class EventMemberSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = EventMember
        fields = ["id","event","email","role","user","created_at"]
        read_only_fields = ["id","user","created_at"]

    def validate_role(self, value):
        if value not in ("REVIEWER", "GUEST"):
            raise serializers.ValidationError("role must be REVIEWER or GUEST")
        return value


class WorkshopSerializer(serializers.ModelSerializer):
    animator = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Workshop
        fields = ["id","event","title","description","animator","start_datetime","end_datetime","created_at"]
        read_only_fields = ["id","animator","created_at"]

    def validate(self, attrs):
        start = attrs.get("start_datetime", getattr(self.instance, "start_datetime", None))
        end = attrs.get("end_datetime", getattr(self.instance, "end_datetime", None))
        if start and end and end <= start:
            raise serializers.ValidationError("end_datetime must be after start_datetime")
        return attrs
