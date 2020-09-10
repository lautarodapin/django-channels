from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .serializers import UserSerializer


@receiver(signal=post_save, sender=User)
def anunciar_nuevo_usuario(sender, instance, created, **kwargs):
    print('Anunciar nuevo usuario')
    if created:
        serializer = UserSerializer(instance)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "users", serializer.data
        )