#coding=utf-8
from os import path
from datetime import datetime
import time

from django.conf import settings
from django.utils.translation import ugettext as _
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from git import *

from models import Repository
from utils import get_repository_dirs 

repository_root = getattr(settings,'GIT_REPOSITORY_ROOT', None)

def index(request):    
    if repository_root:
        repositories = []        
        for dir in get_repository_dirs(repository_root):
            repo = Repo(dir)           
            repo_path = dir.replace(repository_root,'')
            repositories.append(Repository(repo_path, 
            repo.description,
            time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(repo.head.commit.authored_date))))           
        #TODO: something
        return render_to_response('djangogit/index.dj',
                              {'repositories':repositories})
    else:
        return HttpResponse('Please setup the `GIT_REPOSITORY_ROOT` property on settings.py')
    
def repository(request,repo_path):
    if repo_path:        
        repo_path = path.join(repository_root, repo_path)
        repo = Repo(repo_path)  
        commits = list(repo.iter_commits(max_count=10))   
        print len(commits)     
        return render_to_response('djangogit/repository.django.html',
                              {'commits':commits})
    else:
        return HttpResponse('')
    