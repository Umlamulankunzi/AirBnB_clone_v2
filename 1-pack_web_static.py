#!/usr/bin/python3
"""Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Create the archive using tar command
    print("Packing web_static to {}".format(archive_path))
    result = local("tar -czvf {} web_static".format(archive_path))

    if result.succeeded:
        size = os.stat(archive_path).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_path, size))
        return archive_path

    return None
