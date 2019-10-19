import factory
from django.conf import settings
from django.utils import timezone

from .models import Events, Registration


class EventsFactory(factory.DjangoModelFactory):
    class Meta:
        model = Events

    date = timezone.now()


class RegistrationFactory(factory.DjangoModelFactory):
    class Meta:
        model = Registration


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL
