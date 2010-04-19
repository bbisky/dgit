#coding=utf-8
from os import path
from datetime import datetime
import time
import cStringIO, StringIO

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
            try:
                desc = repo.description
            except:
                desc = 'no description'
            repositories.append(Repository(repo_path, 
            desc,
            time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(repo.head.commit.authored_date))))           
        #TODO: something
        return render_to_response('djangogit/index.django.html',
                              {'repositories':repositories})
    else:
        return HttpResponse('Please setup the `GIT_REPOSITORY_ROOT` property on settings.py')
    
def repository(request,repo_path):
    if repo_path:         
        repo_abs_path = path.join(repository_root, repo_path)
        repo = Repo(repo_abs_path)  
        commits = list(repo.iter_commits(max_count=10))         
        return render_to_response('djangogit/repository.django.html',
                              {'commits':commits,
                               'repo_path':repo_path})
    else:
        return HttpResponse('')
    
def commit_view(request,repo_path,sha):
    if repo_path:          
        repo_abs_path = path.join(repository_root, repo_path)
        repo = Repo(repo_abs_path)  
        if repo:
            commit = repo.commit(sha)        
        return render_to_response('djangogit/commit.django.html',
                              {'commit':commit,'repo_path':repo_path})
    else:
        return HttpResponse('')
    
def commit_diff(request,repo_path,sha):
    if repo_path:          
        repo_abs_path = path.join(repository_root, repo_path)
        repo = Repo(repo_abs_path)  
        if repo:
            commit = repo.commit(sha)
        diffs =  commit.diff('HEAD~1',create_patch=True)#.iter_change_type('M')
        
        return render_to_response('djangogit/commitdiff.django.html',
                              {'commit':commit,'repo_path':repo_path,'diffs':diffs},
                              context_instance=RequestContext(request))
    else:
        return HttpResponse('')
    
def tree_view(request,repo_path,sha,from_path=None):
    if repo_path:        
        repo_abs_path = path.join(repository_root, repo_path)
        repo = Repo(repo_abs_path)  
        if repo:
            commit = repo.commit(sha) 
            #不能使用repo.tree
            tree = commit.tree
            if from_path:
                tree = tree/from_path
            if tree.type == 'tree':
                #render tree
                return response_tree(repo_path,commit,tree)
            else:
                #render blob
                return blob_raw(request,tree)
                return response_blob(request,repo_path,commit,tree) 
    
    return HttpResponse('No such repository')
    
def blob_view(request,repo_path,sha,from_path=None):
    if repo_path:        
        repo_abs_path = path.join(repository_root, repo_path)
        repo = Repo(repo_abs_path)  
        if repo:
            commit = repo.commit(sha) 
            #不能使用repo.tree
            tree = commit.tree
            if from_path:
                tree = tree/from_path            
            if tree.type == 'blob':
                #render blob
                filetype = tree.mime_type
                if filetype in text_types:
                    filetype = "text"
                elif filetype.find('/') >= 0:
                    #use the mime main type
                    filetype = filetype[:tree.mime_type.find('/')]                
                return response_blob(request,repo_path,commit,tree,filetype)
                
    return HttpResponse('No such repository')
    

def response_tree(repo_path,commit,tree):    
    return render_to_response('djangogit/tree.django.html',
                                {'commit':commit,
                                'tree':tree,
                                'repo_path':repo_path})

def response_blob(request,repo_path,commit,blob_obj,filetype):
    return render_to_response('djangogit/blob.django.html',
                            {'commit':commit,                            
                            'repo_path':repo_path,
                            'blob':blob_obj,
                            'filetype':filetype,
                            },
                            context_instance=RequestContext(request))

def blob_raw(request,repo_path,sha,from_path):
    if repo_path:        
        repo_abs_path = path.join(repository_root, repo_path)
        repo = Repo(repo_abs_path)  
        if repo:
            commit = repo.commit(sha)             
            tree = commit.tree
            if from_path:
                blob = tree/from_path            
                if blob.type == 'blob':
                    buf = cStringIO.StringIO()    
                    blob.stream_data(buf)   
                    return HttpResponse(buf.getvalue(),blob.mime_type)  
    raise Http404()


#the text mimetypes can use SyntaxHighlighter without startwith 'text'
text_types = ['application/x-javascript']     