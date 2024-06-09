from django import template
from django.conf import settings
from django.contrib.auth.models import Group


register = template.Library()
 
@register.filter
def has_occupation(user, occupation):
    if user.employee:
        return user.employee.occupation.name == occupation 
    else:
        return False
    
    
@register.filter
def has_group(user, group):
    if user.groups:
        return user.groups.name == group 
    else:
        return False