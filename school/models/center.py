from django.db import models

class Center(models.Model):
    center_name = models.CharField(max_length=255)
    center_number = models.CharField(max_length=255, unique=True)
    center_address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.center_name