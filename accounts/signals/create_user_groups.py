from django.contrib.auth.models import  Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_user_groups(sender, **kwargs):

    group_names = (
        ("Super User", 0),
        ("Admin", 0),
        ("Teacher", 0),
        ("Student", 0),
        ("Guardian", 0),
        ("Adminstrator", 0),
    )
    for group_name in group_names:
        Group.objects.get_or_create(
            name=group_name[0]
        )
