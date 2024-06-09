from django.db import models

class Movement(models.Model):
    MOVEMENT_CHOICES = (('Promotions', 'Promotions'), ('Transfer In', 'Transfer In'), ('Transfer Out', 'Transfer Out'))
   
    school_member = models.ForeignKey('accounts.SchoolMember', on_delete=models.CASCADE, related_name='movements')
    movement_type = models.CharField(max_length=255, choices=MOVEMENT_CHOICES)
    movement_date = models.DateTimeField(null=True, blank=True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.school_member} {self.movement_type}'