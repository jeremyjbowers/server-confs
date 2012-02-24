import datetime
import os

from fabric.api import *
from fabric.contrib.console import confirm

WSGI_PATH       = '/data/projects/python/wsgi/my_project.wsgi'
LOCAL_CODE_ROOT = '/data/projects/python/my_project'

def prod():
    '''
    Set the hosts to our production server hosts.
    '''
    env.hosts   = ['12.23.34.45',]

def whoami():
    '''
    Test function; see who I am.
    '''
    run('whoami')
    

def touch_wsgi():
    '''
    Touch the wsgi file for this project.
    '''
    run('touch %s' % WSGI_PATH)
    
def git_pull():
    '''
    Pull down the latest changes from git.
    '''
    with cd(LOCAL_CODE_ROOT):
        run('git pull origin master')
    
