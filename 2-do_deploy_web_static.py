#!/usr/bin/python3
"""Distributes an archive to your web servers, using the function do_deploy"""
from fabric.contrib import files
from fabric.api import env, put, run
import os


env.hosts = ['54.89.26.161', '54.236.43.219']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """Deploys archive files to webserver"""
    if not os.path.exists(archive_path):
        return False

    no_ext_archive_path = archive_path.split('.')[0]
    fname = no_ext_archive_path.split('/')[1]
    dest = '/data/web_static/releases/' + fname

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dest))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(fname, dest))
        run('rm -f /tmp/{}.tgz'.format(fname))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dest))
        return True

    except Exception:
        return False
