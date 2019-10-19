from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from registration.serializers import EventListSerializer, EventDetailSerializer, RegistrationSerializer
from registration.models import Events, Registration


class EventListView(generics.ListAPIView):
    """
    API endpoint that shows all events
    """
    queryset = Events.objects.all()
    serializer_class = EventListSerializer


class EventDetailView(generics.RetrieveAPIView):
    """
    API endpoint shows detail information about one event
    """
    queryset = Events.objects.all()
    serializer_class = EventDetailSerializer


class CreateRegistrationView(generics.CreateAPIView):
    """
    API endpoint creates Registration instance
    """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = (IsAuthenticated,)
