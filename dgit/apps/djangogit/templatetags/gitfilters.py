#coding=utf-8
from os import path
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

def localtime(value): 
    return datetime.fromtimestamp(value)   
    

register.filter(localtime)


def brush(value):
    """
    filetype to SyntaxHighlighter brush
    """
    name,ext = path.splitext(value)
    ext = ext.lower()
    result = {
        '.txt':  "plain",
        '.py':   "python", 
        '.cs':   "csharp",      
        #TODO: add all file type  
    }
    if result.has_key(ext):
        return result[ext]
    else:
        return "plain"
    
register.filter(brush)