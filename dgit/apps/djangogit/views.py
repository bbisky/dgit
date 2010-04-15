#coding=utf-8

from django.conf import settings
from django.utils.translation import ugettext as _
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response

from git import *

from models import Repository
from utils import get_repository_dirs 

def index(request):
    if hasattr(settings,'GIT_REPOSITORY_ROOT'):
        repositories = []
        repository_root = settings.GIT_REPOSITORY_ROOT
        for dir in get_repository_dirs(repository_root):
            repo = Repo(dir)
            repositories.append(Repository(repo.git_dir, repo.description,''))
            print  repo.head.commit.authored_date
        return render_to_response('djangogit/index.dj',
                              {'repositories':repositories})
    else:
        raise Http404