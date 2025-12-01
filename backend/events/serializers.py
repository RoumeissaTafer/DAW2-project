from rest_framework import serializers 
from .models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'admin',
            'title',
            'description',
            'start_date',
            'end_date',
            'location',
        ]
        read_only_fields = ['id', 'admin']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['admin'] = request.user
        return super().create(validated_data)
