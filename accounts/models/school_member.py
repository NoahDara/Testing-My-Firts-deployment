from django.db import models


from django.contrib.auth.models import AbstractUser

from school.models.address import Address

class SchoolMember(models.Model):
    GENDER_CHOICES = (("Male", "Male"), ("Female", "Female"))

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    STATUS_CHOICES = (
        ('Permanent', 'Permanent'), 
        ('Students on Attachment', 'Students on Attachment'),
        ('Graduate Trainees', 'Graduate Trainees'), 
        ('Contract', 'Contract')
    )



    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=255, choices=BLOOD_GROUP_CHOICES, default='A+')
    member_id = models.CharField(max_length=255, unique=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    occupation = models.ForeignKey("school.Occupation", on_delete=models.CASCADE, related_name='members')
    image = models.ImageField(upload_to='member_images/', null=True, blank=True)
    address = models.ManyToManyField(Address, related_name='member_addresses', blank=True)
    program = models.ForeignKey('school.Program', on_delete=models.CASCADE, related_name='programs', null=True, blank=True)
    parent = models.ManyToManyField('school.Parent', related_name='student_parents', blank=True)
    sibling = models.ManyToManyField('school.Sibling', related_name='student_siblings', blank=True)
    school = models.ForeignKey('school.Center', on_delete=models.CASCADE, related_name='school', null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True) 
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    joining_date = models.DateTimeField(null=True, blank=True) 
    date_of_birth = models.DateTimeField(null=True, blank=True)   
    status = models.CharField(max_length=255, choices=STATUS_CHOICES) 
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
