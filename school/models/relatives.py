from django.db import models

from accounts.models import SchoolMember

class Parent(models.Model):
    parent = models.ForeignKey('accounts.SchoolMember', on_delete=models.CASCADE, related_name='parent_relation', null=True, blank=True)
    relationship = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    

    def __str__(self) -> str:
        return str(self.parent)

class Sibling(models.Model):
    sibling = models.ForeignKey('accounts.SchoolMember', on_delete=models.CASCADE, related_name='sibling_relation', null=True, blank=True)
    relationship = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    

    def __str__(self) -> str:
        return str(self.sibling)
