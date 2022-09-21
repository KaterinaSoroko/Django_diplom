from django.db import models
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver


@receiver(models.signals.pre_save, sender=User)
def hash_password(sender, instance, **kwargs):
    if (instance.id is None) or ((sender.objects.get(id=instance.id).password) != instance.password):
       instance.set_password(instance.password)
