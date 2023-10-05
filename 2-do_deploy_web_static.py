#!/usr/bin/python3
"""Distributes an archive to my web servers, using the function do_deploy"""
import os
from fabric.api import env, put, run, sudo


env.hosts = ['54.89.26.161', '54.236.43.219']
env.user = 'ubuntu'

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ dir on the web server
        put(archive_path, "/tmp/")

        # Extract archive to:
        # /data/web_static/releases/<archive_filename_without_ext> on web server
        filename = os.path.basename(archive_path)
        foldername = "/data/web_static/releases/" + os.path.splitext(filename)[0]
        run("mkdir -p {}".format(foldername))
        run("tar -xzf /tmp/{} -C {}".format(filename, foldername))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(filename))

        # Move the contents of the extracted folder to the parent folder
        run("mv {fdname}/web_static/* {fdname}".format(fdname=foldername))

        # Remove the now empty web_static folder
        run("rm -rf {}/web_static".format(foldername))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current linked to the new version
        run("ln -s {} /data/web_static/current".format(foldername))

        return True

    except Exception as e:
        return False
