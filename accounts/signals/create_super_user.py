from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from accounts.models.users import User

@receiver(post_save, sender=User)
def assign_superuser_group(sender, instance, created, **kwargs):

    if created and instance.is_superuser:

        super_user_group, _ = Group.objects.get_or_create(name='Super User')

        instance.groups.clear() 
        
        instance.groups.add(super_user_group) 