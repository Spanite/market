from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Client

@receiver(post_save, sender=User)
def post_save_create_client(sender, instance, create, **kwargs):
    if created:
        Client.objects.create(User=instance)
    instance.Client.save()


going123

