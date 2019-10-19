from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('registration/', views.CreateRegistrationView.as_view(), name='registration'),
]
