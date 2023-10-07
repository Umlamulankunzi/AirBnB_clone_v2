#!/usr/bin/python3
"""Create and distributes an archive to web servers"""
import os.path
import time
from fabric.api import local
from fabric.operations import env, put, run

env.hosts = ['54.89.26.161', '54.236.43.219']
env.user = 'ubuntu'


def do_pack():
    """Generate a tgz archive from web_static directory

    And places archive in created director versions"""
    try:
        local("mkdir -p versions")
        local(
            "tar -cvzf versions/web_static_{}.tgz web_static/".format(
                time.strftime("%Y%m%d%H%M%S")))
        return "versions/web_static_{}.tgz".format(
            time.strftime("%Y%m%d%H%M%S"))

    except Exception:
        return None


def do_deploy(archive_path):
    """Deploys a tar archive to web servers"""
    if not os.path.isfile(archive_path):
        return False

    try:
        filename = archive_path.split("/")[-1]
        directory = ("/data/web_static/releases/" + filename.split(".")[0])
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(directory))
        run("tar -xzf /tmp/{} -C {}".format(filename, directory))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}/".format(directory, directory))
        run("rm -rf {}/web_static".format(directory))
        run('rm -rf /data/web_static/current')
        run("ln -s {} /data/web_static/current".format(directory))
        print("Deployment done")
        return True
    except Exception:
        return False


def deploy():
    """Create and deploy an archive to web servers"""
    try:
        path = do_pack()
        return do_deploy(path)
    except Exception:
        return False
