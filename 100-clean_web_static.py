#!/usr/bin/python3
"""Fabric file that cleans up  old archives from server"""
from fabric.api import local, run, env


env.hosts = ['54.89.26.161', '54.236.43.219']
env.user = 'ubuntu'


def do_clean(number=0):
    """Cleans up old archives"""

    number = int(number) if not isinstance(number, int) else number
    number = 2 if number == 0 else number + 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
