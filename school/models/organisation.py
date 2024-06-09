from django.db import models
from django.db.models import Q
class Organisation(models.Model):
    title = models.CharField(max_length=255, unique=True)

    director = models.ForeignKey('accounts.SchoolMember', on_delete=models.CASCADE, null=True, blank=True, related_name='organisation',
                                 limit_choices_to=Q(role='Adminstrator'))
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title