from django.db import models

from accounts.models import SchoolMember
from school.models.subject import Subject
from school.models.academic_plan import AcademicTerm


class ProgramStructure(models.Model):
    academic_term = models.ForeignKey(AcademicTerm, related_name='program_subjects', on_delete=models.CASCADE, blank=True)
    program_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_due = models.DateField(max_length=255, blank=True, null=True)
    total_amount = models.FloatField(default=1.0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.academic_term)


class Program(models.Model):
    program_name = models.CharField(max_length=255)
    program_code = models.CharField(max_length=255, unique=True)
    program_abbr = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    structures = models.ManyToManyField(ProgramStructure, related_name='program_structures', blank=True)
    subjects = models.ManyToManyField(Subject, related_name='program_subjects', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        first_program_structure = self.program_structure.first()

        if first_program_structure:
            first_academic_term = first_program_structure.academic_term.first()

            if first_academic_term:
                return f"{self.program_name} - {first_academic_term.year}"
            
        return self.program_name

    def get_academic_term(self):
        from school.models.academic_plan import AcademicTerm
        return AcademicTerm.objects.filter(program_structure__program=self).first()

    def get_program_teacher(self):
        from accounts.models import SchoolMember  # Move import here
        return SchoolMember.objects.filter(program=self, is_active=True, is_available=True, is_staff=True).first()

    def get_program_monitor(self):
        from accounts.models import SchoolMember  # Move import here
        return SchoolMember.objects.filter(program_monitor=self, is_active=True, is_available=True, is_staff=True).first()

    def get_program_monitress(self):
        from accounts.models import SchoolMember  # Move import here
        return SchoolMember.objects.filter(program_monitress=self, is_active=True, is_available=True, is_staff=True).first()
