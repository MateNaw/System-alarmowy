from django.db import models
from datetime import datetime
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class Measurement(models.Model):
    localization = models.IntegerField()
    temperature = models.IntegerField()
    gas = models.IntegerField()
    alarm = models.BooleanField(default=False)
    windows = models.BooleanField(default=False)
    time = models.DateTimeField(default=datetime.now)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)
    if not created:
        Token.objects.get(user=instance).delete()
        Token.objects.create(user=instance)
