from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    member = models.OneToOneField('accounts.SchoolMember', on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.member:
            return f"User: {self.member.first_name} {self.member.last_name}"
        else:
            return f"User: {self.username}"

User._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'