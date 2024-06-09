from django.db import models

from accounts.models import SchoolMember

class Subject(models.Model):

    subject_name = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=255, unique=True)
    subject_teacher = models.ForeignKey(SchoolMember, on_delete=models.CASCADE, related_name='program_teachers', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.subject_name