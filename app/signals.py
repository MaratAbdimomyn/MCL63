from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import get_object_or_404

@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    Post.objects.create(user=instance)