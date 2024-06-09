from django.db.models.signals import post_migrate
from django.dispatch import receiver

from school.models.occupation import Occupation


@receiver(post_migrate)
def create_occupations(sender, **kwargs):

    occupatio_names = (
        ("Director", 0),
        ("Principal", 0),        
        ("Head Matser", 0),
        ("Head Mistress", 0),
        ("Burser", 0),
        ("Deputy Head", 0),
        ("Senior Teacher", 0),
        ("Sports Director", 0),
        ("Examiner", 0),
        ("Class Teacher", 0),
        ("Teacher", 0),
        ("Head Boy", 0),
        ("Head Girl", 0),
        ("Vice Head Girl", 0),
        ("Vice Head Boy", 0),   
        ("Senior Prefect", 0),
        ("Prefect", 0),
        ("Monitor", 0),
        ("Monitress", 0),  
        ("Student", 0),            
    )
    for occupation_name in occupatio_names:
        Occupation.objects.get_or_create(
            name=occupation_name[0]
        )