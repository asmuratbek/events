from registration.models import Events, Registration
from rest_framework import serializers


class EventListSerializer(serializers.HyperlinkedModelSerializer):
    has_users = serializers.SerializerMethodField()

    class Meta:
        model = Events
        fields = ['title', 'text', 'date', 'has_users']

    def get_has_users(self, obj):
        return obj.registration_set.exists()


class EventDetailSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.SerializerMethodField()

    class Meta:
        model = Events
        fields = ['title', 'text', 'date', 'users']

    def get_users(self, obj):
        return [registration.user.username for registration in obj.registration_set.all()]


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['user', 'event']
