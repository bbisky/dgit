#coding=utf-8
from datetime import datetime

from django import template

register = template.Library()

def timestampsince(value): 
    t = datetime.fromtimestamp(value)
    from django.utils.timesince import timesince
    if not value:
        return u''
    try:        
        return timesince(t)
    except (ValueError, TypeError):
        return u''
    
register.filter(timestampsince)