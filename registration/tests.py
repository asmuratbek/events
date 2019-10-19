from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.
from registration.factories import UserFactory, EventsFactory, RegistrationFactory

client = APIClient()


class TestEventEndpoints(TestCase):

    def setUp(self) -> None:
        self.user = UserFactory(username='Муратбек')
        self.event1 = EventsFactory()
        self.event2 = EventsFactory()
        self.reserve = RegistrationFactory(event=self.event1, user=self.user)

    def test_list_events_return_200(self):
        response = client.get(reverse("api:event_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(2, len(response.json()))

    def test_if_events_have_user_and_if_events_are_not_have_user(self):
        response = client.get(reverse("api:event_list"))
        self.assertTrue(response.json()[0]['has_users'])
        self.assertFalse(response.json()[1]['has_users'])

    def test_event_detail_page_return_200_and_return_list_of_users(self):
        response = client.get(reverse("api:event_detail", kwargs={'pk': self.event1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['users'][0], self.user.username)


class TestReserveEndpoint(TestCase):

    def setUp(self) -> None:
        self.user = UserFactory()
        self.event = EventsFactory()
        self.url = reverse("api:registration")

    def test_return_403_if_user_is_not_authenticated(self):
        client.logout()
        response = client.post(self.url, {"user": self.user.pk, "event": self.event.pk})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_return_201_if_registration_is_created(self):
        client.force_authenticate(user=self.user)
        response = client.post(self.url, {"user": self.user.pk, "event": self.event.pk})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
