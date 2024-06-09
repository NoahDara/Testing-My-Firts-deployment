from django.db import models

class AcademicYear(models.Model):
    year = models.IntegerField()
    start_date = models.DateTimeField(null=True, blank=True)   
    end_date = models.DateTimeField(null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.year
    

class AcademicTerm(models.Model):
    year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='academic_year', null=True, blank=True)
    term_name = models.CharField(max_length=255)
    start_date = models.DateTimeField(null=True, blank=True)   
    end_date = models.DateTimeField(null=True, blank=True) 
    fees_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.year}  {self.term_name}"   