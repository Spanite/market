from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Client


def post_save_create_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(User=instance)

post_save.connect(Client, sender=User)