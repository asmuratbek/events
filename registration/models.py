from django.db import models
from django.conf import settings


class Events(models.Model):
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-date']

    title = models.CharField(max_length=255, verbose_name='Title of event')
    text = models.TextField()
    date = models.DateTimeField(verbose_name='Date')


class Registration(models.Model):
    class Meta:
        verbose_name = 'Registration'
        verbose_name_plural = 'Registrations'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    event = models.ForeignKey(Events, on_delete=models.CASCADE, verbose_name='Event')
