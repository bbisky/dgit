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
        '.cs':   "csharp",
        '.css': "css",
        '.html': "html",
        '.js':  "jscript",
        '.php':   "php",
        '.py':   "python",        
        '.txt':  "plain",
        '.aspx': "xml",
        '.ascx': "xml",
        '.xml':  "xml",
        '.xhtml': "xml",
        '.xslt':     "xml",
        '.html': "xml",
        '.csproj': "xml",
        #TODO: add all file type  
    }
    if result.has_key(ext):
        return result[ext]
    else:
        return "plain"
    
register.filter(brush)

#def data(value):
#    print isinstance(value,unicode)
#    return unicode(value,'gb2312')
#register.filter(data)